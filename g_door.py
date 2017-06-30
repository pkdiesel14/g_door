# Imports
import RPi.GPIO as GPIO
import time
import sys
from subprocess import call

# Basic GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configure Pins as follows:
# GPIO 5, 6 Inputs for the switches, configured as pullups
# then switch is mechanized to ground.
# 0 = Closed
# 1 = Open
#
# GPIO 10 is a status LED
# GPIO 9 and 11 are used to drive a relay to press a door opener switch
# 
# Initializing states is critical

GPIO.setup(5, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, GPIO.PUD_UP)

GPIO.setup(10,GPIO.OUT) #Status LED
GPIO.setup(9, GPIO.OUT, initial=1) #press switch for door 1
GPIO.setup(11, GPIO.OUT, initial=1) #press switch for door 2


def menu_gen():
    call(["clear"])
    print(" ")    
    print("***************     Main Menu for Garage Door     ***********")
    print(" ")
    print("Select one of the following choices")
    
    print("A: Return System Status")
    print("B: Open/Close Door 1")
    print("C: Open/Close Door 2")
    print("D: Raspberry Pi Information")
    print("E: Not currently used")
    print("")
    print("Q or cntrl-C to exit program")

def menu_a():
    door1 = GPIO.input(5)
    door2 = GPIO.input(6)
    print("")
    print("")
    print("return system status and information")
    print("")
    print("Door 1 is: %s " % ("CLOSED" if door1 else "OPEN"))
    print("Door 2 is: %s " % ("CLOSED" if door2 else "OPEN"))
    print("")
    
    try:
        tmp = raw_input("Press <enter> to continue")
    except:
        tmp = input("Press <enter> to continue")    

    
print("***********    INITALIZING    ***********")

for x in range(3):  #flash LED 3X
    GPIO.output(10, GPIO.HIGH) 
    time.sleep(1)
    GPIO.output(10, GPIO.LOW)
    time.sleep(1)

# main loop, loop here until Q or Cntrl-C is selected)
var1 = ""
while(var1 != 'q'):
    menu_gen()     # Generate the Menu
    #  Need to try raw_input first to see if program is running with Python 2.7
    #  versus Python 3.X
    try:
        var1 = raw_input("Make your selection: ")
    except:
        var1 = input("Make your selection: ")
    print("you have slected", var1)
    if var1 == 'a' or var1 == 'A':
        print("A Selected")
        menu_a()
    elif var1 == 'b' or var1 == 'B':
        print("Moving Door 1 !!!")
        GPIO.output(9, GPIO.LOW)
        time.sleep(2)
        GPIO.output(9, GPIO.HIGH)
    elif var1 == 'c' or var1 == 'C':
        print("Moving Door 2 !!!")
        GPIO.output(9, GPIO.LOW)
        time.sleep(2)
        GPIO.output(9, GPIO.HIGH)
    elif var1 == 'd' or var1 == 'D':
        print("D has been selected")
    elif var1 == 'e' or var1 == 'E':
        print("E has been selected")
    elif var1 == 'q' or var1 == 'Q':
        print("**********  Shutting Down  **********")
        break
    else:
        print("Invalid input, try again")
        
    
            
    

    
