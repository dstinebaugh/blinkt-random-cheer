#!/usr/bin/env python

import random
import time

try:
    import requests
except ImportError:
    exit("This script requires the requests module\nInstall with: sudo pip install requests")

from blinkt import set_clear_on_exit, set_pixel, show


set_clear_on_exit()

while True:
    pixels = random.sample(range(8), random.randint(1, 5))
    r = requests.get('http://api.thingspeak.com/channels/1417/field/2/last.json')
    col = r.json()['field2']
    r, g, b = tuple(ord(c) for c in col[1:].lower().decode('hex'))
    for i in range(8):
        if i in pixels:
            set_pixel(i, r, g, b)
        else:
            set_pixel(i, 0, 0, 0)
    show()
    time.sleep(1)

