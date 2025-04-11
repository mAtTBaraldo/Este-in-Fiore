# IoT
# MQTT e PYTHON
# SUBSCRIBER
# DATI FORMATO JSON
#
# Simulazione
# Misura temperatura in una serra
# Topic: casamiarosa/cucina/sensore/tu
# Ricezione dati IoT dal broker formato JSON
#
# Test:
# avviare casa_dc_publisher.py
# utilizzare come URL 127.0.0.1:5000 o IP:5000
# utilizzare curl -v http://127.0.0.1:5000
# utilizzare curl http://127.0.0.1:5000  -o risposta.json per acquisire la pagina
#
from flask import Flask, render_template, request, redirect
from datetime import timedelta, datetime
from time import time
import json
import socket

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
print("connesso")

client_soc, indirizzo = serversocket.accept()
def ricevi():
    try: 
        dati = client_soc.recv(bufferdati).decode()
        #effettuo la somma di tutte le medie dei rilevamenti
        if dati:
            dati = json.loads(dati)
            print(dati)
        
        dati = json.dumps(dati, indent=4)
        return dati
               
    except KeyboardInterrupt:
        print(invioNumero)
        print("\nPROGRAMMA INTERROTTO")



#
app = Flask(__name__)

# Parametri
refresh = 5                                   # Tempo in secondi per il refresh della dashboard
# 
# Route
#  

@app.route('/')
def landing():
    dati = ricevi()
    trovato = False
    Dati_per_template = json.loads(dati)              # Conversione da JSON
    Dati_per_template['REFRESH'] =  refresh                             # Agggiunta refresh
    print(Dati_per_template)
    return render_template(f"realtime.html",**Dati_per_template)   # Passaggio dizionario con scompattamento

@app.route('/seleziona', methods=["GET"])
def seleziona():
    cabina = request.args.get("cabina", type=int)
    pagina = request.args.get("selettore", type=int)
    if pagina == 1:
        return redirect(f"/realtime?cabina={cabina}")
    elif pagina == 2:
        return redirect(f"/day?cabina={cabina}")
    

@app.route('/realtime') # root route (default page)
def dashb():
    trovato = False
    Dati_per_template = json.loads(dati)              # Conversione da JSON
    Dati_per_template['REFRESH'] =  refresh                             # Agggiunta refresh

    return render_template(f"realtime.html",**Dati_per_template)   # Passaggio dizionario con scompattamento

# Avvio del server web integrato per eseguire l'applicazione
# rende l'APP accessibile all'indirizzo specificato o di default
# e blocca l'esecuzione dello script finché il server non viene chiuso
#
app.run(host='0.0.0.0',port=5000)
#
print ("Server interrotto manualmente con CTRL+C")
#
# LTR - marzo 2021 - revisione 2024
# enneci
