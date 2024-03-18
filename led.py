import RPi.GPIO as GPIO
import time


def showLight(id, speed):
    GPIO.output(id, GPIO.HIGH)
    time.sleep(float(speed))
    GPIO.output(id, GPIO.LOW)
    time.sleep(float(speed))

channel_list = (8,12,18)
# GPIO.output(chan_list, GPIO.LOW) # all LOW
# GPIO.output(chan_list, (GPIO.HIGH,GPIO.LOW))  # first HIGH, second LOW

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_list, GPIO.OUT)
# GPIO.setup(12, GPIO.OUT)
# GPIO.setup(8, GPIO.OUT)

while True:
    user_input = input("Enter blinks number: ('0' to quit): ")

    if user_input == '0':
        break

    speed = input("Set speed in seconds: ")    
    counter = 0
    while counter < int(user_input):
       showLight(channel_list, speed)
       counter+=1

GPIO.cleanup()


