import time
import random
from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw, ImageFont
import utils
import setup as su
import images as img


class Graduation:
    #def __init__(self):
    def start(self,draw,image,disp):
        draw.rectangle((0, 0,240, 240), outline=0, fill=(255,255,255))
        image.paste(img.graduate, (0,0))
        #image.paste(img.me, (230-open_del,120), img.me)
        su.disp.image(image)
        time.sleep(0.5)

        open_del = 0
        

        while True:
            draw.rectangle((0, 0,240, 240), outline=0, fill=(255,255,255))
            image.paste(img.company,(0,0))
            image.paste(img.me_g, (open_del,120-open_del), img.me_g)
            su.disp.image(image)
            time.sleep(0.5)
            open_del+=20
            
            if open_del >90:
                image.paste(img.company,(0,0))
                #draw.rectangle((0, 0,240, 240), outline=0, fill=(255,255,255))
                large = img.me.crop((0,0,120,120))
                large = large.resize((150, 150))
                image.paste(large, (90,70),large)
                draw.rectangle((0, 180,240, 240), outline=0, fill=0) # Draw a black filled box to clear the image.
                draw.text((0, 182), "Where company could \n i work for?\n Naver? Samsung?", font=img.fnt, fill=(255,255,255))
                su.disp.image(image)
                time.sleep(2)
                image.paste(img.passed, (0,0), img.passed)
                image.paste(large, (90,90),large)
                su.disp.image(image)
                time.sleep(4)
                while True:
                    draw.rectangle((0, 0,240, 240), outline=0, fill=(255,255,255))
                    image.paste(img.employed,(0,0))
                    image.paste(img.me_em, (-10,0), img.me_em)
                    su.disp.image(image)
                    time.sleep(0.5)
                    image.paste(img.employed,(0,0))
                    image.paste(img.me_em, (10,0), img.me_em)
                    su.disp.image(image)
                    time.sleep(0.5)
   






                break

            


        return image
        