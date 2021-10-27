#! /usr/bin/python
import json 
import time
import os
#import random
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType

def hpcorrect(color):
  # led human perception korrektur
  gc = [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,10,10,10,10,11,11,11,12,12,12,13,13,13,14,14,15,15,15,16,16,17,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27,28,28,29,29,30,31,31,32,32,33,34,34,35,36,37,37,38,39,39,40,41,42,43,43,44,45,46,47,47,48,49,50,51,52,53,54,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,72,73,74,75,76,77,79,80,81,82,83,85,86,87,88,90,91,92,94,95,96,98,99,100,102,103,105,106,108,109,110,112,113,115,116,118,120,121,123,124,126,128,129,131,132,134,136,138,139,141,143,145,146,148,150,152,154,155,157,159,161,163,165,167,169,171,173,175,177,179,181,183,185,187,189,191,193,196,198,200,202,204,207,209,211,214,216,218,220,223,225,228,230,232,235,237,240,242,245,247,250,252]
  return gc[color]

#Convert pywal hex values into RGB for OpenRGB
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))

#Open pywal JSON File
mydir = os.path.expanduser("~/.cache/wal/colors.json")
with open(mydir) as colors_json:
  pywalData = json.load(colors_json)

#Set all RGB color variables 
allColours = pywalData['colors']

RGBColourSets = [hex_to_rgb(allColours['color0']), hex_to_rgb(allColours['color1']), hex_to_rgb(allColours['color2']), hex_to_rgb(allColours['color3']), hex_to_rgb(allColours['color4']), hex_to_rgb(allColours['color5']), hex_to_rgb(allColours['color6']), hex_to_rgb(allColours['color7']), hex_to_rgb(allColours['color8']), hex_to_rgb(allColours['color9']), hex_to_rgb(allColours['color10']), hex_to_rgb(allColours['color11']), hex_to_rgb(allColours['color12']), hex_to_rgb(allColours['color13']), hex_to_rgb(allColours['color14']), hex_to_rgb(allColours['color15'])]

mainboardcolor = RGBColourSets[6]
leftcolor = RGBColourSets[1]
middlecolor = RGBColourSets[4]
rightcolor = RGBColourSets[2]

client = OpenRGBClient()

for x in range(0,15):
  print(x)
  print(RGBColourSets[x])

client.clear() # Turns everything off

time.sleep(0.1)
motherboard = client.get_devices_by_type(DeviceType.MOTHERBOARD)[0]

motherboard.set_mode('direct')
motherboard.zones[1].resize(56)

#Mainboard
for x in range(0,3):
  motherboard.zones[1].leds[x].set_color(RGBColor(mainboardcolor[0],mainboardcolor[1],mainboardcolor[2]))
for x in range(3,5):
  motherboard.zones[1].leds[x].set_color(RGBColor(rightcolor[0],rightcolor[1],rightcolor[2]))


#rechts
for x in range(5,12):
  motherboard.zones[1].leds[x].set_color(RGBColor(hpcorrect(round(rightcolor[0])),hpcorrect(round(rightcolor[1])),hpcorrect(round(rightcolor[2]))))

#links
for x in range(26,30):
  motherboard.zones[1].leds[x].set_color(RGBColor(hpcorrect(round(middlecolor[0])),hpcorrect(round(middlecolor[1])),hpcorrect(round(middlecolor[2]))))

#mitte
for x in range(49,55):
  motherboard.zones[1].leds[x].set_color(RGBColor(hpcorrect(round(leftcolor[0])),hpcorrect(round(leftcolor[1])),hpcorrect(round(leftcolor[2]))))
