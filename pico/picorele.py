# Raspberry Pico
# Gestione Relè
#
# Modulo dello script orto.py
#
# Script: picorele.py
#
from machine import Pin
import time
"""
Relè

- Collega (+) terminale al GPIO specificato
- Collega (-) terminale a GND
"""
#
# Funzioni
#
def configura(PIN):
    global rele
    rele = Pin(PIN, Pin.OUT)
    return rele
#
def accendi():
    rele.value(1)           # Accendi il LED
    return
#
def spegni():
    rele.value(0)          # Spegni il LED
    return
#
# febbraio 2025
# enneci www.enneci.cloud
# Licenza CC BY-NC