# Test acquisizione temperatura e umidità
# dal sensore DHT11/DHT22
#
# Raspberry Pico WH
#
# Script: orto_sensore_dht.py
#
import machine
import time
#
import misurazione_tu         # Acquisizione temperatura (gradi) e umidità (percentuale) dell'aria
                              # sensore DHT11 oppure DHT22
#
# Parametri
#
PIN_S_DHT = 2           # PIN sensore di temperatura e umidità dell'aria DHT11/DHT22
TEMPO_MISURAZIONE = 2   # secondi - acquisizione della misurazione
#
SENSORE = "DHT11"       # Utilizzo sensore DHT11 oppure DHT22
#
while True:
    temperatura_aria,umidita_aria = misurazione_tu.leggi_temp_umi(PIN_S_DHT,SENSORE)   # Acquisizione misura dal sensore DHT11/DHT22
    time.sleep(TEMPO_MISURAZIONE)
    print ( temperatura_aria,umidita_aria)
#
# enneci - febbraio 2025
# laboratorio LTR - IIS Euganeo - Este (PD)
# enneci www.enneci.cloud
# Licenza CC BY-NC