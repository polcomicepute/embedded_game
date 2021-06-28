import time
import random
from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw, ImageFont
import utils
import setup as su
import images as img
import Episode.Graduation as Graduation

import Episode.Game_1 as Game_1

graduation = Graduation.Graduation()
game1 = Game_1.Game1()

class School:
    def __init__(self):
        self.background = img.back[0]
        self.stage =0
        
    def walk(self, draw, image, delta_x, delta_y, backup_x, backup_y, st_check,clear):
        #draw.rectangle((0, 0,240, 240), outline=0, fill=(255,255,255))
        state_x = 0+delta_x
        state_y = 360+delta_y #430
        target = self.background.crop((state_x,state_y,state_x+360,state_y+360)) #start from upper_point(0,430) and down_point(360,690) 
        target = target.resize((240, 240)) #resize image (360,360) -> (240,240)

        #check outside 
        delta_x,delta_y=utils.check_outside(target,delta_x,delta_y,backup_x,backup_y,(0,0,0)) 

        #background 
        image.paste(target, (0,0)) 
        print(state_x,state_y)
        


        if (state_x<630 and state_x >= st_check[1][0]) and state_y <= st_check[1][1]: #chagne to array !! 
            if clear[1] ==1:
                print(state_x, state_y)
                print("Already Finish!! ")
                self.stage=0
                return self.stage, image, delta_x, delta_y
            print("errerrerr")
            #go to stage1 
            background = img.back[1]
            self.stage = 1 
            print("come_game1")
            ##
            image=game1.start(draw,image,su.disp)
            # state_x=0
            # state_y=0
            # delta_x=0
            # delta_y=0 #stage0's var initialize
        elif (state_x<1800 and state_x >= st_check[3][0]):
            image = graduation.start(draw,image,su.disp)
        else:
            self.stage=0
        return self.stage, image, delta_x, delta_y
    