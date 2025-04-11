# Raspberry Pico
# Gestione led
#
# Modulo dello script orto.py
#
# Script: picoled.py
#
from machine import Pin
import time
"""
LED con resistenza

- Collega l'anodo (+) terminale corto del LED al GP specificato
- Collega il catodo (-) terminale lungo del LED a GND
"""
#
# Funzioni
#
def configura(PIN):
    global led
    led = Pin(PIN, Pin.OUT)
    return led

def accendi():
    led.value(1)           # Accendi il LED
    
    return
def spegni():
    led.value(0)          # Spegni il LED
    
    return
#
# novembre 2024
# enneci www.enneci.cloud
# Licenza CC BY-NC