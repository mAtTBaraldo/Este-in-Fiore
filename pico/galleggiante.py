# Gestione sensore umidità del terreno
# Modulo dello script orto.py
# 
# Raspberry Pico WH
# Utilizzo libreria ADC
#
# Script: misurazione_terreno.py
#
"""
Sensore di umidità Joy-It

- Collegamento VCC a 3.3V del Pico
- Collegamento GND a GND del Pico
- Collegamento OUT a GPn (ADC) del Pico
"""
from machine import Pin, ADC   # ADC conversione analogico-digitale
import time
#
"""
Il sensore è analogico, quindi deve essere collegato ad un pin analogico,
a cui è associato un convertitore analogico/digitale ADC.
I Pin analogici a bordo del Pico sono 4, di cui 3 accessibili all’esterno: GP26 (ADC0), GP27 (ADC1), e GP28 (ADC2)
e 1 ADC connesso direttamente al sensore di temperatura integrato nel microcontrollore.
"""
#
def leggi_livello(PIN):
    moisture_sensor = ADC(PIN) 
    moisture_value = moisture_sensor.read_u16()  # Lettura valore ADC (0-65535)
    return moisture_value
#
# enneci - febbraio 2025
# laboratorio LTR - IIS Euganeo - Este (PD)
# enneci www.enneci.cloud
# Licenza CC BY-NC
