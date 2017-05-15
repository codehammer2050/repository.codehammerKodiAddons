import xbmcaddon
import xbmcgui
import os
from src import piusv
from __future__ import print_function

import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()
logger.addHandler(logging.FileHandler('test.log', 'a'))
print = logger.info

print('yo!')



piusv = piusv.PiUSV()

status = piusv.statusByte()

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

line1 = "Hello World!"
line2 = "We can write anything we want here"

def get_resolution():
    try:
        win = xbmcgui.Window()
        return win.getWidth() + 'x' + win.getHeight()
    except TypeError:
        return '1920x1080'
print(status)
print(get_resolution())

xbmcgui.Dialog().ok(addonname, line1, status,get_resolution())
