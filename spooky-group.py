#!/usr/bin/python

import datetime
import phue
import random
import time
import sys

from helpers import is_working_hours, STAIRS_GROUP


b = phue.Bridge(sys.argv[1])

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

group_id = STAIRS_GROUP
while is_working_hours():
    # White lights only, so no hue
    # hue = random.randint(0, 6000)
    # sat = random.randint(200, 255)
    brightness = random.randint(3,100)
    # on = (True if random.randint(0, 10) > 1 else False)
    on = True
    transition_time = random.randint(3, 10) if on else 0
    command =  { 'on' : on, 'bri' : brightness, }

    # print("Group {} getting command {} with transition time of {}".format(group_id, command, transition_time))
    b.set_group(group_id, command, transitiontime=transition_time)

    delay_to_next_event = (float(transition_time)/5) + random.randrange(0, 1) + 0.5
    # print('Waiting for {} seconds'.format(delay_to_next_event))
    time.sleep(delay_to_next_event)


b.set_group(group_id, { 'on': False })
