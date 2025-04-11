# Gestione LED onboard Pico WH
#
# Modulo dello script orto.py
#
# Raspberry Pico WH
# Accensione del LED interno all'avvio dello script di gestiona
# Spegnimento del LED interno alla fine dello script di gestione
#
# Script:armo_disarmo.py
#
import machine
#
def arma():
    led_interno = machine.Pin("LED", machine.Pin.OUT)
    led_interno.on()
    return
def disarma():
    led_interno = machine.Pin("LED", machine.Pin.OUT)
    led_interno.off()
    return
#
# enneci - febbraio 2025
# laboratorio LTR - IIS Euganeo - Este (PD)
# enneci www.enneci.cloud
# Licenza CC BY-NC