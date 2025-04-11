# Gestione delle misure effettuate
# con trasformazione in dato IoT nel formato JSON
#
# Modulo dello script orto.py
#
# Raspberry Pico WH
# Utilizzo libreria json
#
# Script: gestione_dati.py
#
import json
import socket
#

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = "192.168.5.206"
portasocket = 9992
bufferdati = 1024
clientsocket.connect((hostname,portasocket))
    
    
def trasmissione(UTPSOPRA,UTPSOTTO,TA,UA,N):
    dati_dizionario = { "umiditaterrenosopra": UTPSOPRA,"umiditaterrenosotto": UTPSOTTO, "temperaturaaria": TA, "umiditaaria": UA,"rilevazione": N}
    dato_json = json.dumps(dati_dizionario).encode()
    clientsocket.send(dato_json)
    print (dato_json)   # Trasmissione (simulazione)
    print ()
    return
#
# enneci - febbraio 2025
# laboratorio LTR - IIS Euganeo - Este (PD)
# enneci www.enneci.cloud
# Licenza CC BY-NC