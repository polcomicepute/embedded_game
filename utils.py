
import time
import random
from colorsys import hsv_to_rgb

import Episode.Game_1 as Game_1
import setup as su
import images as img



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

def enroll(image,draw):
    #opening
    image.paste(img.opening, (0,0))
    su.disp.image(image)
    time.sleep(2)
    open_del = 0
    while (230-open_del) > 120: #walking 
        draw.rectangle((0, 0,240, 240), outline=0, fill=(255,255,255))
        image.paste(img.back[1],(0,0))
        image.paste(img.me, (230-open_del,120), img.me)
        su.disp.image(image)
        time.sleep(0.5)
        open_del+=30
    #talking
    image.paste(img.back[1]),(0,0)
    large = img.me.crop((0,0,120,120))
    large = large.resize((150, 150))
    image.paste(large, (70,50),large)
    draw.rectangle((0, 145,240, 240), outline=0, fill=0) # Draw a black filled box to clear the image.
    draw.text((0, 147), "This is my \n university, KAU! \n I'm nervous!", font=img.fnt_big, fill=(255,255,255))
    su.disp.image(image)
    time.sleep(2)
         

def graduate(image,draw):
    #graduate
    draw.rectangle((0, 0,240, 240), outline=0, fill=(255,255,255))
    image.paste(img.graduate, (0,0))
    su.disp.image(image)
    time.sleep(1)
    open_del=0
    while open_del <90:
        draw.rectangle((0, 0,240, 240), outline=0, fill=(255,255,255))
        image.paste(img.company,(0,0))
        image.paste(img.me_g, (open_del,120-open_del), img.me_g)
        su.disp.image(image)
        time.sleep(0.5)
        open_del+=20
    #Employment Preparation
    image.paste(img.company,(0,0))
    large = img.me.crop((0,0,120,120))
    large = large.resize((150, 150))
    image.paste(large, (90,70),large)
    draw.rectangle((0, 180,240, 240), outline=0, fill=0) # Draw a black filled box to clear the image.
    draw.text((0, 182), "Where company could \n i work for?\n Naver? Samsung?", font=img.fnt, fill=(255,255,255))
    su.disp.image(image)
    time.sleep(2)
    #passed
    image.paste(img.passed, (0,0), img.passed)
    image.paste(large, (90,90),large)
    su.disp.image(image)
    time.sleep(3)
    #employment success!!
    for i in range(open_del):
        draw.rectangle((0, 0,240, 240), outline=0, fill=(255,255,255))
        image.paste(img.employed,(0,0))
        image.paste(img.me_em, (10*((-1)^(open_del%2))+10,0), img.me_em)
        su.disp.image(image)
        time.sleep(0.5)
        open_del-=1