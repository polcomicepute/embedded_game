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

game1 = Game_1.Game1()

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

backup_x=[0,0,0,0,0,0]
backup_y=[0,0,0,0,0,0] 
delta_x =0
delta_y =0

state_x=0
state_y=0 #stage location var 

fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)

#background = Image.open('/home/pi/Embedded/embedded_game/img/HangPark.png')
me = Image.open('/home/pi/Embedded/embedded_game/img/Me3.png')

hangmap =  Image.open('/home/pi/Embedded/embedded_game/img/Map3.png')

back = [Image.open('/home/pi/Embedded/embedded_game/img/Map3.png'), Image.open('/home/pi/Embedded/embedded_game/img/HangPark.png'), ]
push_A=False
push_B=False


while True:
    
    #image.paste(background, (0,0))
    #draw.rectangle((0, 0, width, height), outline=0, fill=0) # Draw a black filled box to clear the image.
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
        push_A=True
    if not su.button_B.value:  # left pressed
        push_B=True
    
    if stage != 0:
        image.paste(background, (0,0))
        #image.paste(me, (delta_x,delta_y), me)

    if stage == 0:#In stage 0
        state_x=0+delta_x
        state_y=430+delta_y
        target = hangmap.crop((state_x,state_y,state_x+360,state_y+360)) #start from upper_point(0,430) and down_point(360,690) 
        target = target.resize((240, 240)) #resize image (360,360) -> (240,240)

        delta_x,delta_y=utils.check_outside(target,delta_x,delta_y,backup_x[0],backup_y[0],(0,0,0)) 

        image.paste(target, (0,0)) #background 
        
        backup_x[0] = delta_x
        backup_y[0] = delta_y
        if state_x >= st_check[1][0] and state_y <= st_check[1][1]: 
            #go to stage1 
            background = back[1]
            stage = 1 
            print("come_game1")
            ##
            image=game1.start(draw,image,su.disp)
            state_x=0
            state_y=0
            delta_x=0
            delta_y=0 #stage0's var initialize

    elif stage ==1: #In stage 1 
        state_x=delta_x
        state_y=delta_y+130
        image, delta_x,delta_y=game1.walk(draw,image,delta_x,delta_y,backup_x[1],backup_y[1])
        backup_x[1] = delta_x
        backup_y[1] = delta_y
        # if state_x>230 and state_y>240: #turn back to stage0
        #     delta_x =backup_x[0]
        #     delta_y =backup_y[0]+60
        #     stage =0
    elif stage ==2:#In stage 2
        pass
    elif stage ==3:#In stage 3
        pass
    elif stage ==4:
        pass#In stage 4
    image.paste(me, (80, 80),me) #me 

    push_A=False
    push_B=False
   
    
    
        
    su.disp.image(image)

