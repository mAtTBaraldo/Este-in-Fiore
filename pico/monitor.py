# Gestione display LCD 12x2 protocollo I2C
# Modulo dello script orto.py
#
# Raspberry Pico WH
# Utilizzo libreria lcd_api e pico_i2c_lcd
#
# Script: monitor.py
#
from machine import Pin, I2C
import time
import lcd_api       # Libreria LCD
import pico_i2c_lcd  # Libreria per I2C LCD
#
def display(testo,pinsda,pinscl):
    # Inizializza I2C SDA e SCL
    i2c = I2C(0, scl=Pin(pinscl), sda=Pin(pinsda), freq=400000)

    # Inizializza il display LCD
    lcd = pico_i2c_lcd.I2cLcd(i2c, 0x27, 2, 16)  # Indirizzo 0x27, 2 righe, 16 colonne

    # Scrive un messaggio sul display
    lcd.clear()
    lcd.putstr(testo)
    time.sleep(2)
    return

