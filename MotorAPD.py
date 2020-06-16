import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ControlPin = [7, 11, 13, 15]

for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

seq = [  [1,0,0,0],
         [1,1,0,0],
         [0,1,0,0],
         [0,1,1,0],
         [0,0,1,0],
         [0,0,1,1],
         [0,0,0,1],
         [1,0,0,1]  ]

for i in range(512):
    for halfstep in range(8):
        for pin in range(4):
            GPIO.output(ControlPin[pin], seq[halfstep][pin])
        time.sleep(0.01)

GPIO.cleanup()

#zdroj: Stepper Motor Control with the Raspberry Pi [online]. 17. 7. 2013
#[cit. 2020-06-16]. Dostupné z:
#https://www.youtube.com/watch?v=Dc16mKFA7Fo
