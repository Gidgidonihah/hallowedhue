#!/usr/bin/python

import phue
import random
import time
import sys

from helpers import is_working_hours, STAIRS_GROUP


b = phue.Bridge(sys.argv[1])

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

group_id = STAIRS_GROUP
light_ids = [int(numeric_string) for numeric_string in b.get_group(10,'lights')]

while is_working_hours():

    # White lights only. no need for hue/sat
    # hue = random.randint(0, 6000)
    # sat = random.randint(200, 255)
    light_id = random.choice(light_ids)
    brightness = random.randint(3,70)
    on = True
    transition_time = random.randint(3, 10) if on else 0
    command =  {
        'transitiontime' : transition_time,
        'on' : on,
        'bri' : brightness,
    }

    # print("Group {} getting command {} with transition time of {}".format(group_id, command, transition_time))
    b.set_light(light_id, command)

    delay_to_next_event = (float(transition_time)/75) + (float(random.randrange(10, 100))/1000.0)
    # print('Waiting for {} seconds'.format(delay_to_next_event))
    time.sleep(delay_to_next_event)

# Turn off the lights
for light in light_ids:
    b.set_light(light, { 'on': False })
