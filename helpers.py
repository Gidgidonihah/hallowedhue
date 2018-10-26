import datetime


BEDROOM_GROUP = 2
STAIRS_GROUP = 10

def is_working_hours():
    # Only operate the effect between 7pm and 2am
    now = datetime.datetime.now()
    return (now.hour >= 19 or now.hour < 2)
