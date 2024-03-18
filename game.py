import RPi.GPIO as GPIO
import time
import random

GREEN = 12
RED = 18
YELLOW = 8

GPIO.setmode(GPIO.BCM)

GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)

number = random.randint(1, 100)
gussed = 0 
speed = 1.5
while number != gussed:
    print('Please guess a number 1-100')
    #get input from user
    user_input = input()
    #validate user input
    if (user_input.isnumeric()):
        #convert input to integer (number)
        gussed = int(user_input)
        if number == gussed:
            print('Right!')

            #Show green light for 3 seconds
            GPIO.output(GREEN, GPIO.HIGH)
            time.sleep(speed)
            GPIO.output(GREEN, GPIO.LOW)
        elif number < gussed:
            print('Too high!')
            #Show red light for 3 seconds
            GPIO.output(RED, GPIO.HIGH)
            time.sleep(speed)
            GPIO.output(RED, GPIO.LOW)
        else:
            print('Too low!')
            #Show yellow light for 3 seconds
            GPIO.output(YELLOW, GPIO.HIGH)
            time.sleep(speed)
            GPIO.output(YELLOW, GPIO.LOW)
    else: 
        print('enter only number please')

