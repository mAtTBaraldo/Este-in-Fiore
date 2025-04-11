# Gestione sensore temperatura e umidità
# Modulo dello script orto.py
#
# Modulo dello script orto.py
#
# DHT11 (celeste) o DHT22 (bianco)
# Raspberry Pico WH
# Utilizzo libreria dht
#
# Script: misurazione_tu.py
#
from machine import Pin
import dht 
#
def leggi_temp_umi(N_PIN,SENSORE):
    #
    if SENSORE == "DHT11":
        sensor = dht.DHT11(Pin(N_PIN))     # Sensore celeste
    else:
        SENSORE = dht.DHT22(Pin(N_PIN))    # sensore bianco
    #
    sensor.measure()
    temp = sensor.temperature()         # gradi Celsius
    umi = sensor.humidity()             # percentuale di umidità relativa
    return temp,umi
#
# print(leggi_temp_umi(2))
#
# Main
#
# enneci - ottobre 2024
# laboratorio LTR - IIS Euganeo - Este (PD)
# enneci www.enneci.cloud
# Licenza CC BY-NC