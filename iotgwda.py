#SIMULAZIONE DI UN UNICO DC CHE INVIA LA RILEVAZIONE DI TEMPERATURA E UMIDITA AL DA IL QUALE CALCOLA LA MEDIA DEI DUE DATI OGNI 
# TEMPO_RILEVAZIONE E LI SALVA UN FILE. IL COLLEGAMENTO TRA I DUE AVVIENE TRAMITE SOCKET.
#RILEVAZIONE DEI DATI DAL RASPBERRYPICO
#Progetto numero 3
#Autori: Ambrosi Alberto e Ambrosi Alex
#5AI
#14/11/2024
#Collegamento tra client e server tramite socket
#iotgwda.py

import socket
import json
import datetime
import paho.mqtt.client as mqtt


#FUNZIONI--------------------------




#Try except per ricevere l'eccezione del programma interroto in caso di ctrl+c

#leggo il file parametri.json
fileParametri = "configurazione/parametri.json"
with open (fileParametri, "r") as file:
    parametri = json.load(file)   
    
#creo il socket
hostname = parametri.get("IP_SERVER")
portasocket = parametri.get("PORTA_SERVER")
maxconnessionicoda = 5
famiglia = socket.AF_INET
tipo = socket.SOCK_STREAM
bufferdati = 1024
serversocket = socket.socket(famiglia,tipo)
serversocket.bind((hostname, portasocket))
serversocket.listen(maxconnessionicoda)

print(f"SERVER IN ASCOLTO SU INDIRIZZO: {hostname}")
print(f"SERVER IN ASCOLTO SU PORTA: {portasocket}")


BROKER_HOST  = parametri.get("BROKER")
PORTA_BROKER = parametri.get("PORTA_BROKER")
print(PORTA_BROKER)
TOPIC = parametri.get("TOPIC")
QOS = 0                                        
KEEPALIVE = 60

client = mqtt.Client()
client.connect(BROKER_HOST, PORTA_BROKER, KEEPALIVE)
client.on_connect = on_connect

client.loop_start()

nRilevazioni = 0
invioNumero = 0
temperaturaTotale = 0
umiditaTotale = 0

#salvo il numero(tempo) di rilevazioni da effettuare prima di salvare nel file
tempoInvio = (parametri.get("TEMPO_INVIO")*60) / parametri.get("TEMPO_RILEVAZIONE")
misura = 0 

try:
    while True:

        client_soc, indirizzo = serversocket.accept()

        #invio al dc dei parametri utili
        parametriJSON = {
            "TEMPO_RILEVAZIONE": parametri.get("TEMPO_RILEVAZIONE"),
            "N_DECIMALI": parametri.get("N_DECIMALI")
        }
        
        client_soc.send(json.dumps(parametriJSON).encode())
        
        while True:
            dati = client_soc.recv(bufferdati).decode()
            #effettuo la somma di tutte le medie dei rilevamenti
            if dati:
                dati = json.loads(dati)
                print(dati)
            if not dati:
                break
            
            dati = json.dumps(dati, indent=4)
           
except KeyboardInterrupt:
    print(invioNumero)
    print("\nPROGRAMMA INTERROTTO")

client.loop_stop()
client.disconnect()