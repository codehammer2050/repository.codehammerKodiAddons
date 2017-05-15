import xbmcaddon
import xbmcgui
import os
from src import piusv


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



xbmcgui.Dialog().ok(addonname, line1, status,get_resolution())
