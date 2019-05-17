import gpiozero as zero

from time import sleep

cor = .002
maxPW=(2.0+cor)/1000
minPW=(1.0-cor)/1000

servo = zero.Servo(17, min_pulse_width=minPW, max_pulse_width=maxPW)

while True:
    
    servo.min()
    print("min")
    print(servo.value)
    sleep(2)
    servo.max()
    print("max")
    print(servo.value)
    sleep(2)
    servo.mid()
    print("mid")
    print(servo.value)
    sleep(2)
