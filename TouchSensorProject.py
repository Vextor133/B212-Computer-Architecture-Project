from gpiozero import LED, Button
from time import sleep

touch_sensor = Button(17, pull_up=False)


led1 = LED(22)
led2 = LED(27)

try:
    while True:
        if touch_sensor.is_pressed:
            print('Touch Sensor is activiated')
            led1.off()  
            led2.on()   
        else:
            led1.on()
            led2.off()

        sleep(0.5)# B212-Computer-Architecture-Project
