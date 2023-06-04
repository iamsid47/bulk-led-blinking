import RPi.GPIO as GPIO
import time

led_1 = 1
led_2 = 2
led_3 = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)
GPIO.setup(led_3, GPIO.OUT)


def blink():
    GPIO.output(led_1, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led_1, GPIO.LOW)
    time.sleep(1)


def illu():
    GPIO.output(led_1, GPIO.HIGH)
    GPIO.output(led_2, GPIO.HIGH)
    GPIO.output(led_3, GPIO.HIGH)


def illu_2():
    GPIO.output(led_1, GPIO.HIGH)
    GPIO.output(led_2, GPIO.LOW)
    GPIO.output(led_3, GPIO.LOW)


try:
    while True:
        userInp = str(input("Enter: "))

        if userInp == "b":
            blink()
        elif userInp == "g":
            illu()
        elif userInp == "y":
            illu_2()
        else:
            print("Invalid user input, try again.")

except KeyboardInterrupt:
    GPIO.cleanup()
