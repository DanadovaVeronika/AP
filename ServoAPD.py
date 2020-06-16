import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
servo = GPIO.PWM(12, 50)

servo.start(0)
print("Waiting for 2 seconds.")
time.sleep(2)

print("Rotating 180 degrees in 10 steps.")

duty = 2

while duty <= 12:
    servo.ChangeDutyCycle(duty)
    time.sleep(0.3)
    servo.ChangeDutyCycle(0)
    time.sleep(0.7)
    duty = duty + 1
    
time.sleep(2)

print("Turnung back to 90 degrees for 2 seconds.")
servo.ChangeDutyCycle(7)
time.sleep(0.5)
servo.ChangeDutyCycle(0)
time.sleep(1.5)

print("Turning back to 0 degrees.")
servo.ChangeDutyCycle(2)
time.sleep(0.5)
servo.ChangeDutyCycle(0)

servo.stop()
GPIO.cleanup()
print("Goodbye.")

#zdroj: Raspberry Pi Servo Motor Control [online]. 12. 1. 2020 
#[cit. 2020-06-16]. Dostupné z: 
#https://www.youtube.com/watch?v=xHDT4CwjUQE
