# Test sensore umidità del terreno
# 
# Raspberry Pico WH
#
# Script: orto_terreno.py
#
import machine
import time
#
import misurazione_terreno    # Acquisizione misura umidità del terreno
#
# Parametri
#
PIN_S_MOISTURE = 26    # PIN sensore di umidità del terreno
#
TEMPO_MISURAZIONE = 2   # secondi - acquisizione della misurazione
#
while True:
    umidita_terreno = misurazione_terreno.leggi_umi(PIN_S_MOISTURE)  # Acquisizione misura dal sensore mouisture
    print(umidita_terreno)               
    #
    time.sleep(TEMPO_MISURAZIONE)       # Acquisizione dati 
#
# enneci - febbraio 2025
# laboratorio LTR - IIS Euganeo - Este (PD)
# enneci www.enneci.cloud
# Licenza CC BY-NC