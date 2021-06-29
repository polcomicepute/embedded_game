import time
import random
from colorsys import hsv_to_rgb
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
import setup as su
import utils
import images as img
import Episode.School as School
import Episode.Game_1 as Game_1


game1 = Game_1.Game1()
school = School.School()

class currentStage:
    def __init__(self):
        self.stage = 0
        #remember last position
        self.backup_x=[0,0,0,0,0,0]
        self.backup_y=[0,0,0,0,0,0] 
        #how many move using the buttons
        self.delta_x =0
        self.delta_y =0

        self.st_check = [(0,0),(250, 300),(520, 910), (1700, 380),(560,860)]
        self.clear=[0,0,0,0,0,0] #check complete the Games

    def start(self,image,draw):
        print("main",self.stage)
        if self.stage == 0:#In self.stage 0 #make func of hangmap ? 
            #background = img.back[0]
            self.stage, image, self.delta_x, self.delta_y = school.walk(draw, image, self.delta_x, self.delta_y, self.backup_x[0], self.backup_y[0],self.st_check,self.clear)
            self.backup_x[0] = self.delta_x
            self.backup_y[0] = self.delta_y
        elif self.stage ==1: #In self.stage 1 
            self.stage, image, self.delta_x, self.delta_y = game1.walk(draw,image,self.delta_x,self.delta_y,self.backup_x[1],self.backup_y[1])
            self.backup_x[1] = self.delta_x
            self.backup_y[1] = self.delta_y
            if self.stage ==0:
                self.clear[1]=1
                self.delta_x =self.backup_x[0]
                self.delta_y =self.backup_y[0]+60
        elif self.stage ==2:#In self.stage 2
            pass
        elif self.stage ==3:#In self.stage 3
            pass
        elif self.stage ==4:#In self.stage 4
            pass
        elif self.stage ==5:#In self.stage 5 = graduation
            utils.graduate(image, draw)
        elif self.stage==-1:# self.stage==-1 , Game Over
            print("game over")
            draw.rectangle((0, 0,240, 240), outline=0, fill=0) # Draw a black filled box to clear the image.
            draw.text((0, 147), "Game Over", font=img.fnt_big, fill=(255,255,255))
            su.disp.image(image)
        image.paste(img.me, (80, 80),img.me) #me 
        su.disp.image(image)