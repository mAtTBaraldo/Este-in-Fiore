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
#
import picoled                # Gestione LED
#
# Parametri
#
PIN_S_LED = 3          # PIN LED (simulazione relè per irrigazione)
TEMPO_IRRIGAZIONE = 5   # secondi - durata irrigazione
#
picoled.configura(PIN_S_LED)  # Assegnazione PIN GPIO al LED
picoled.spegni()              # Led spento (nessuna irrigazione)
#
while True:
    #
    picoled.accendi()               # Led acceso (inizio irrigazione)
    print ("LED acceso")
    time.sleep(TEMPO_IRRIGAZIONE)
    picoled.spegni()                # Led spento (nessuna irrigazione)
    print ("LED spento")
    time.sleep(TEMPO_IRRIGAZIONE)
#
# enneci - febbraio 2025
# laboratorio LTR - IIS Euganeo - Este (PD)
# enneci www.enneci.cloud
# Licenza CC BY-NC