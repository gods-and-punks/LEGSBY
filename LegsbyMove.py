import gpiozero as zero
from time import sleep

big = 100
lil = 0
mid = int((big-lil)*(2/5))


servo = zero.AngularServo(17, min_angle = lil, max_angle = big)
while True:
    servo.angle = big
    sleep(1)
    print("big")
    servo.angle = mid
    sleep(1)
    print("mid")
    servo.angle = lil
    sleep(1)
    print("lil")
