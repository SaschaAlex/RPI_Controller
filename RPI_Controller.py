
import RPi.GPIO as GPIO

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)


GPIO.setup(11,GPIO.OUT)  # Currant output 3.3V
GPIO.output(11,0) # Make sure the Pin is off


print("Welcome!, You can press CTRL+C for exit the program!")

try:
    while(True):
        request = input("press : (1 = on , 0 = off): ")
        if(len(request) ==1):
            GPIO.output(11,int(request[0]))
            if(int(request[0]) == 0):
                print("GPIO 11 is off!")
            else:
                if(int(request[0]) == 1):
                    print("GPIO 11 is on!")
                else:
                    GPIO.output(11,0)
                    print("invalid input!")
finally:
    GPIO.output(11,0)
    GPIO.cleanup()
