import Adafruit_DHT
import RPi.GPIO as GPIO
import drivers
from time import sleep
import board

display = drivers.Lcd()
dhtSensor = Adafruit_DHT.DHT11
pin = 14

try:
    while True:
        try:
            humidity, temp_c = Adafruit_DHT.read_retry(dhtSensor, pin)
        except RuntimeError:
            print("RuntimeError, trying again...")
            continue
        print("Writing to display")
        display.lcd_display_string("Temperature:", 1)
        display.lcd_display_string(format(temp_c, ".2f")+"°C", 2)
        display.lcd_display_string("Humidity:", 3)
        display.lcd_display_string(format(humidity, ".2f"), 4)
        sleep(2)

except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()
    display.lcd_display_string("Clearing", 1)
    sleep(1)
    display.lcd_clear()
