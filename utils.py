
import time
import random
from colorsys import hsv_to_rgb
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import Episode.Enroll as Enroll
import Episode.Game_1 as Game_1
import setup as su



me_center= (120,170)
def check_outside(target, delta_x,delta_y,get_pixel_x,get_pixel_y, color):
    #if i met the pixel of black, stop 
    length =len(target.getpixel(me_center))
    if length ==3:
        r,g,b= target.getpixel(me_center)
    else:
        r,g,b,a= target.getpixel(me_center)
    if (r==color[0]) and (g == color[1]) and (b ==color[2]): 
        print("Block!!")
        delta_x =get_pixel_x
        delta_y =get_pixel_y
    return delta_x,delta_y