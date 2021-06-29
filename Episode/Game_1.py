import time
import random
from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw, ImageFont
import utils
import setup as su
import images as img




# Create the display

class Game1:
    def __init__(self):
        self.dup= img.room.copy()
        
        self.rand_x=random.randint(50,1450)
        self.rand_y=random.randint(50,950)
        #random.seed()

        self.correct = 0
        self.wrong = 0 
        self.stage =1

        self.right=False

        self.rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        self.quiz_list=["Could a function of python get \n the only one return value?","How to make the \n constructor in python?", "How to use modules in python?", "Which of the following\n statements is correct? "]
        self.quiz_answer1=[("O",(0,255,0),True),("def constructor",(255,0,0),False), ("import", (0,255,0), True), ("set can add or remove elements,", (0,255,0), True)]
        self.quiz_answer2=[("X",(255,0,0),False), ("def __init__",(0,255,0),True), ("module",(255,0,0), False), ("Elements of a set aren't unique",(255,0,0), False)]

    
    def start(self,draw,image,disp):
        self.correct = 0
        self.wrong = 0 
        self.stage =1

        image.paste(img.start_img, (0,0))
        disp.image(image)
        time.sleep(0.5)
        #
        image.paste(img.back_1, (0,0))
        large = img.pro_kill.crop((0,0,120,120))
        large = large.resize((240, 240))
        image.paste(large, (35,0),large)
        draw.rectangle((0, 145,240, 240), outline=0, fill=0) # Draw a black filled box to clear the image.
        draw.text((0, 147), "Hello, HangGong! \n Welcome to KAU \n aka.HELL \n For 4 years, \nYou can't escape!!!", font=img.fnt, fill=(255,255,255))
        disp.image(image)
        time.sleep(2.5)
        #
        draw.rectangle((0, 0,240, 240), outline=0, fill=(255,255,255))
        large = img.me.crop((0,0,120,120))
        large = large.resize((240, 240))
        image.paste(large, (35,0),large)
        draw.text((60, 200), "Oh, no!!!!!", font=img.fnt_big , fill=(0,0,0)
        disp.image(image)
        time.sleep(1)
        return image

    def walk(self,draw,image,delta_x, delta_y,backup_x,backup_y):
        state_x=1500-240+delta_x +80
        state_y=1000-240+delta_y +80
        #self.rand_x,self.rand_y = kill's location / state_x,state_y = my location
        print(state_x,state_y,self.rand_x,self.rand_y)
        
        # meet kill professor
        if (self.rand_x -50< state_x and state_x< self.rand_x +50) and (self.rand_y -50< state_y and state_y< self.rand_y +50):
            self.rand_x=random.randint(0,1350)
            self.rand_y=random.randint(0,850)
            random.seed()
            self.dup = img.room.copy()
            #print("meet")
            image.paste(img.room_quiz, (0,0),img.room_quiz) 
            draw.text((self.rand_x+30,self.rand_y), "!!!", font=img.fnt, fill=(255,0,0))
            su.disp.image(image)
            time.sleep(2)
            self.stage = self.quiz(image,draw)

        self.dup.paste(img.pro_kill, (self.rand_x,self.rand_y),img.pro_kill)
        target = self.dup.crop((1500-(240-delta_x),1000-(240-delta_y),1500+delta_x,1000+delta_y)) #start from upper_point(0,430) and down_point(360,690) 

        #prevent to go outside/desk
        delta_x,delta_y=utils.check_outside(target,delta_x,delta_y,backup_x,backup_y,(0,0,0)) 
        delta_x,delta_y=utils.check_outside(target,delta_x,delta_y,backup_x,backup_y,(255,255,255))

        image.paste(target, (0,0)) #background 
        #draw the curcle how many you corrected
        for i in range(self.correct -self.wrong):
            draw.ellipse((i*20,0,i*20+20,20), fill = "#00ff6e" )
        
        return self.stage, image, delta_x, delta_y
    
    def quiz(self,image,draw):
        self.right= False
        rand = random.randint(0,len(self.quiz_list)-1)
        
        while True:
            draw.rectangle((0, 0,240, 240), outline=0, fill=(255,255,255))
            #print(rand)
            image.paste(img.back_1, (0,0))
            large = img.pro_kill.crop((0,0,120,120))
            large = large.resize((240, 240))
            image.paste(large, (35,0),large)
            draw.rectangle((0, 145,240, 240), outline=0, fill=0) # Draw a black filled box to clear the image.
            draw.text((0, 147), self.quiz_list[rand], font=img.fnt_small, fill=(255,255,255))
            
            if not su.button_B.value: 
                self.check(image, draw, -10,self.quiz_answer1[rand])
            if not su.button_A.value: 
                self.check(image, draw, 10, self.quiz_answer2[rand])
            
            #print(self.correct, self.wrong) #check the number of correct or wrong answer 

            # if the answers are wrong at least 3 times, Game over 
            if (self.correct < self.wrong) and (self.wrong>2):
                self.stage = -1 
                image.paste(img.return_1,(0,0),img.return_1)
                su.disp.image(image)
                time.sleep(3)
                return self.stage

            draw.text((0, 190), self.quiz_answer1[rand][0], font=img.fnt_small, fill=(255,255,255))
            draw.text((0, 210), self.quiz_answer2[rand][0], font=img.fnt_small, fill=(255,255,255))
            su.disp.image(image)

            if self.right: #If the answer is right
                time.sleep(0.5)
                draw.rectangle((0, 145,240, 240), outline=0, fill=0) # Draw a black filled box to clear the image.
                draw.text((0, 147), "You are right..' \n Next time will be difficult.\n you'll be wrong!!", font=img.fnt, fill=(255,255,255))
                su.disp.image(image)
                time.sleep(3)
                if (self.correct>self.wrong) and (self.correct > 2):
                    self.stage=0
                    image.paste(img.end_1, (0,0),img.end_1)
                    su.disp.image(image)
                    time.sleep(3)
                return self.stage

    def check(self,image, draw, delt, answer):
        time.sleep(0.5)
        draw.rectangle((0, 200+delt,240, 220+delt), outline=0, fill=answer[1])  # up, green, yes
        self.right = answer[2]
        if self.right:
            self.correct +=1
        else: 
            self.wrong +=1