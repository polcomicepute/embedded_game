import time
import random
from colorsys import hsv_to_rgb
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import Episode.Game_1 as Game_1
import setup as su
import utils
import images as img
import Episode.School as School
#import Episode.Game_1 as Game_1
import currentStage 

#game1 = Game_1.Game1()
curr_stage = currentStage.currentStage()
#enroll=Enroll.Enroll()

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for color.
width = su.disp.width
height = su.disp.height
image = Image.new("RGBA", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Clear display.
draw.rectangle((0, 0, width, height), outline=0, fill=(255, 0, 0))
su.disp.image(image)

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)



utils.enroll(image, draw)
while True: 
    draw.rectangle((0, 0,240, 240), outline=0, fill=(255,255,255))
    if not su.button_U.value:  # up pressed
        curr_stage.delta_y-=20
    if not su.button_D.value:  # down pressed
        curr_stage.delta_y +=20
    if not su.button_L.value:  # left pressed
        curr_stage.delta_x-=20
    if not su.button_R.value:  # right pressed
        curr_stage.delta_x+=20
    if not su.button_C.value:  # center pressed
        pass
    if not su.button_A.value:  # left pressed
        pass
    if not su.button_B.value:  # left pressed
        pass
    

    curr_stage.start(image,draw)



