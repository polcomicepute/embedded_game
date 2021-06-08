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
import utils
import images as img
import Episode.School as School

game1 = Game_1.Game1()
school = School.School()

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

stage = 0
st_check = [(0,0),(250, 300),(520, 910)]

clear=[0,0,0,0,0,0] #check complete the Games

#remember last position
backup_x=[0,0,0,0,0,0]
backup_y=[0,0,0,0,0,0] 

#how many move using the buttons
delta_x =0
delta_y =0

state_x=0
state_y=0 #stage location var 



while True:
    draw.rectangle((0, 0,240, 240), outline=0, fill=0)
    if not su.button_U.value:  # up pressed
        delta_y-=20
    if not su.button_D.value:  # down pressed
        delta_y +=20
    if not su.button_L.value:  # left pressed
        delta_x-=20
    if not su.button_R.value:  # right pressed
        delta_x+=20
    if not su.button_C.value:  # center pressed
        pass
    if not su.button_A.value:  # left pressed
        pass
    if not su.button_B.value:  # left pressed
        pass
    print("main",stage)
    
    if stage == 0:#In stage 0 #make func of hangmap ? 
        #background = img.back[0]
        stage, image, delta_x, delta_y = school.walk(draw, image, delta_x, delta_y, backup_x[0], backup_y[0],st_check,clear)
        backup_x[0] = delta_x
        backup_y[0] = delta_y
    elif stage ==1: #In stage 1 
        stage, image, delta_x, delta_y = game1.walk(draw,image,delta_x,delta_y,backup_x[1],backup_y[1])
        backup_x[1] = delta_x
        backup_y[1] = delta_y
        if stage ==0:
            clear[1]=1
            delta_x =backup_x[0]
            delta_y =backup_y[0]+60
    elif stage ==2:#In stage 2
        pass
    elif stage ==3:#In stage 3
        pass
    elif stage ==4:
        pass#In stage 4
    elif stage ==5:
        pass
    elif stage==-1:# stage==-1 , Game Over
        print("game over")
        draw.rectangle((0, 0,240, 240), outline=0, fill=0) # Draw a black filled box to clear the image.
        draw.text((0, 147), "Game Over", font=img.fnt_big, fill=(255,255,255))
        su.disp.image(image)
        break
    image.paste(img.me, (80, 80),img.me) #me 
        
    su.disp.image(image)

