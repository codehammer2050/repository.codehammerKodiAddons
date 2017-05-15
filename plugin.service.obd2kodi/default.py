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
line3 = status.tostring()

xbmcgui.Dialog().ok(addonname, line1, line2, line3)
