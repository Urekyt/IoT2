from machine import Pin, deepsleep, UART
from time import sleep
import dht

uart = UART(1, 115200)

sensor = dht.DHT11(Pin(14))

def readDHT11():
    try:     
        sensor.measure()
        sleep(2)
        temp = sensor.temperature()
        hum = sensor.humidity()
        return temp, hum
    except OSError as e:
        print("Failed to read sensor:")


uart.write(str(readDHT11))
print(readDHT11())

deepsleep(3600000)