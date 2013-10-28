#!/usr/bin/python

import phue
import random
import time
import sys
b = phue.Bridge(sys.argv[1])

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

while True:
    light = random.randint(1,3)
    wrap = random.randint(0,1)
    hue = random.randint(0, 6000)
    sat = random.randint(200, 255)
    transition_time = random.randint(5, 75)
    delay_to_next_event = (float(transition_time)/1000.0) + (float(random.randrange(10, 100))/1000.0)
    brightness = random.randint(150,254)
    on = (True if random.randint(0, 10) > 1 else False)
    command =  {'transitiontime' : transition_time, 'on' : on, 'bri' : brightness, 'hue': hue, 'sat': sat}
    print("Light %d getting command %s" % (light, str(command)))
    b.set_light(light, command)
    time.sleep(delay_to_next_event)


