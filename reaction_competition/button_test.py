import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

button = 12

GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    if GPIO.input(button) == GPIO.HIGH:
        print("Button connected to pin {button} was pressed.")
        time.sleep(1)