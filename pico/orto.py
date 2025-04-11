# Gestione orto urbano
# 
# Raspberry Pico WH
# Utilizzo di un  sensore di umidità del terreno e
# un sensore di temperatura umidità dell'aria con la simulazione dell'irrigazione
# nel caso di terrreno troppo asciutto per un orto urbano
#
# Script: orto.py
#
import machine
import time
import json
#
import misurazione_tu         # Acquisizione temperatura (gradi) e umidità (percentuale) dell'aria
                              # sensore DHT11 oppure DHT22
#
import picorele               # Gestione relè
import misurazione_terreno    # Acquisizione misura umidità del terreno
import monitor                # Gestione display LCD 12x2
import armo_disarmo           # Gestione LED interno
import gestione_dati          # Gestione dei dati provenienti dai sensori
import galleggiante           # Gestione livello acqua della vasca di irrigazione
import wifi
#
# Parametri Pico
#
wifi.connetti()
f = open('pico.conf',"r")     # Opening JSON file
parametri = json.load(f)      # returns JSON object as a dictionary
f.close()                     # Closing file
#
PIN_S_DHT = parametri["sensoretu"]["pinsegnale"]               # PIN sensore di temperatura e umidità dell'aria DHT11/DHT22
PIN_S_MOISTURE_SOPRA = parametri["sensoreterrenosopra"]["pinsegnale"]     # PIN sensore di umidità del terreno
PIN_S_MOISTURE_SOTTO = parametri["sensoreterrenosotto"]["pinsegnale"]     # PIN sensore di umidità del terreno
PIN_S_RELE = parametri["rele"]["pinsegnale"]                   # PIN relè per irrigazione
PIN_ACQUA =  parametri["sensoreacqua"]["pinsegnale"]           # PIN sensore livello acqua
PIN_CICALINO =  parametri["cicalino"]["pinsegnale"]            # PIN cicalino
SENSORE_TU = parametri["sensoretu"]["tipo"]                    # Utilizzo sensore DHT11 oppure DHT22
PIN_SDA = parametri["display"]["pinsda"]                       # Display SDA I2C
PIN_SCL = parametri["display"]["pinscl"]                        # Display SCL I2C
"""
Calibrazione:
- Esecuzione script calibra_sensore.py che effettua N_MISURAZIONI (20)
  con sensore in aria e inizializzazione della costante CALIBRAZIONE_ARIA
  con la media come intero
  
- Esecuzione script calibra_sensore.py che effettua N_MISURAZIONI (20)
  con sensore in acqua e inizializzazione della costante CALIBRAZIONE_ACQUA
  con la media come intero 
"""
# Valore minimo ADC con misurazione in aria (0 valore minimo ADC)
CALIBRAZIONE_ARIA  = parametri["sensoreterrenosopra"]["calibraaria"]
# Valore massimoADC con misurazione in acqua (65535 valore massimo ADC)
CALIBRAZIONE_ACQUA = parametri["sensoreterrenosotto"]["calibraacqua"]
#
VOLTAGGIO_PICO = 3.3    # Voltaggio PIN Raspberry Pico
#
#SOGLIA_IRRIGAZIONE = 40 # Valore in percentuale. Al di sotto poca acqua, quindi irrigazione
#
TEMPO_AVVIO = 2         # secondi
#TEMPO_IRRIGAZIONE = 10  # secondi - durata irrigazione
TEMPO_MISURAZIONE = 5   # secondi - acquisizione della misurazione
#TEMPO_INERZIA = 2       # secondi - pausa dopo l'irrigazione
#
# Gestione sistema
#
#armo_disarmo.arma()     # Accensione LED interno RPI Pico
#
#picorele.configura(PIN_S_RELE)  # Assegnazione PIN GPIO al relè
#picorele.spegni()               # Relè chiuso nessuna irrigazione
#
#monitor.display("Sistema" + "\n" + "in attivazione",PIN_SDA,PIN_SCL)
time.sleep(TEMPO_AVVIO)
#
n_misurazioni = 0
#gestione_dati.connessione()
while True:
    #controllo_acqua = galleggiante.leggi_livello(PIN_ACQUA)
    #
    """
    gestione poca acqua nella
    vasca per irrigazione
    """
    #
    n_misurazioni = n_misurazioni + 1
    temperatura_aria,umidita_aria = misurazione_tu.leggi_temp_umi(PIN_S_DHT,SENSORE_TU)   # Acquisizione misura dal sensore DHT11/DHT22
    umidita_terreno_sopra = misurazione_terreno.leggi_umi(PIN_S_MOISTURE_SOPRA)               # Acquisizione misura dal sensore mouisture
    umidita_terreno_sotto = misurazione_terreno.leggi_umi(PIN_S_MOISTURE_SOTTO)               # Acquisizione misura dal sensore mouisture
    voltaggio = round((umidita_terreno_sopra / CALIBRAZIONE_ACQUA ) * VOLTAGGIO_PICO,2) # Misura sensore in Volt
    # Trasformazione in percentuale
    #SENSORE SOPRA
    umidita_territorio_percentuale_sopra = 100 - ((umidita_terreno_sopra - CALIBRAZIONE_ACQUA) / (CALIBRAZIONE_ARIA - CALIBRAZIONE_ACQUA) * 100)
    umidita_territorio_percentuale_sopra = max(0, min(100, umidita_territorio_percentuale_sopra))  # Mantiene il valore tra 0 e 100%
    umidita_territorio_percentuale_sopra = int(umidita_territorio_percentuale_sopra)
    #SENSORE SOTTO
    umidita_territorio_percentuale_sotto = 100 - ((umidita_terreno_sotto - CALIBRAZIONE_ACQUA) / (CALIBRAZIONE_ARIA - CALIBRAZIONE_ACQUA) * 100)
    umidita_territorio_percentuale_sotto = max(0, min(100, umidita_territorio_percentuale_sotto))  # Mantiene il valore tra 0 e 100%
    umidita_territorio_percentuale_sotto = int(umidita_territorio_percentuale_sotto)
    #
    """
    UT umidità terreno in percentuale
    TA temperatura aria in grado celsius
    UA umidità relativa dell'aria in percentuale
    V  voltaggio
    """
    #
    #testo_display = "Monitoraggio " + str(n_misurazioni) +"\n" + "UT" + str(umidita_territorio_percentuale) + " TA" + str(temperatura_aria) + " UA" + str(umidita_aria)
    print("Monitoraggio " + str(n_misurazioni))
    testo_sopra   = "SOPRA: " + "UT " + str(umidita_territorio_percentuale_sopra) + "% - Voltaggio " + str(voltaggio)
    testo_sotto   = "SOTTO: " + "UT " + str(umidita_territorio_percentuale_sotto) + "% - Voltaggio " + str(voltaggio)
    testo_aria =  "V - TA " + str(temperatura_aria) + "C° - UA " + str(umidita_aria) + "%"
    #monitor.display(testo_display,PIN_SDA,PIN_SCL)      # Visualizzazione misure su display LCD
    print(testo_sopra)                  # Debug
    print(testo_sotto)
    print(testo_aria)
    gestione_dati.trasmissione(umidita_territorio_percentuale_sopra,umidita_territorio_percentuale_sotto,temperatura_aria,umidita_aria,n_misurazioni)  # Gestione dei dati delle misure
    #
    time.sleep(TEMPO_MISURAZIONE)       # Acquisizione dati non più di una volta al secondo con il DHT11
                                        # mentre non più di una volta ogni 2 secondi con il DHT22
    #
    #if  umidita_territorio_percentuale < SOGLIA_IRRIGAZIONE:
        #picorele.accendi()              # Relè aperto inizio irrigazione
        #testo_display = "UT" + str(umidita_territorio_percentuale) + " < Soglia " + str(SOGLIA_IRRIGAZIONE) + "\n" + "Irrigazione"
        #print(testo_display)            # Debug
        #monitor.display(testo_display,PIN_SDA,PIN_SCL)  # Visualizzazione misura terreno e operazione di irrigazione su display LCD
        #time.sleep(TEMPO_IRRIGAZIONE)
        #picorele.spegni()                # Relè chiuso nessuna irrigazione
        #testo_display = "Irrigato: "  + str(TEMPO_IRRIGAZIONE) + "s" + "\n" + "Fine irrigazione"
        #print()
        #monitor.display(testo_display,PIN_SDA,PIN_SCL)  # Visualizzazione operazione di irrigazione su display LCD
        #time.sleep(TEMPO_INERZIA) 
#
# enneci - febbraio 2025
# laboratorio LTR - IIS Euganeo - Este (PD)
# enneci www.enneci.cloud
# Licenza CC BY-NC