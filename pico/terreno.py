from machine import Pin, ADC
import time
import wifi
sensor = ADC(Pin(28))
readings = []
somma = 0
wifi.connetti("iot","iotpiotp")
try:
   while True:
       for i in range(10):
           reading = sensor.read_u16()
           somma = somma + reading
           readings.append(reading)
           print(readings) 
           time.sleep(1)
       median_value = somma / 10
       if median_value < 400:
           #urequests.get("https://api.telegram.org/bot"+secrets.API+"/sendMessage?text=Gary is thirsty&chat_id="+secrets.ID)
           print("Poca acqua")
       else:
           print("acqua ok")
       time.sleep(3600)
except OSError:
   print("@"*68)
   print("@ Cannot connect to the Wi-Fi, please check your SSID and PASSWORD @")
print("@"*68)