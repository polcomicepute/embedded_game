import time
import random
from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw, ImageFont
import utils
import setup as su



# Create the display

class Game1:
    def __init__(self):
        self.start_img = Image.open('/home/pi/Embedded/embedded_game/img/Game1/Game1_start.png')
        self.professor = Image.open('/home/pi/Embedded/embedded_game/img/Game1/pro1.png')
        self.back_1 = Image.open('/home/pi/Embedded/embedded_game/img/Game1/Map3_G1.png')
        self.me = Image.open('/home/pi/Embedded/embedded_game/img/Me3.png')
        self.room = Image.open('/home/pi/Embedded/embedded_game/img/Game1/Game1_room2.png')
        self.room_quiz = Image.open('/home/pi/Embedded/embedded_game/img/Game1/Quiz.png')
        
        self.dup= self.room.copy()
        
        self.rand_x=random.randint(50,1450)
        self.rand_y=random.randint(50,950)
        random.seed()


        self.fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
        self.fnt_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
        self.rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        self.quiz_list=["Could a function of python get \n the only one return value?","How to make the \n'main' func in Python?"]
        self.quiz_answer1=[("O",(0,255,0),True),("def main",(255,0,0),False)]
        self.quiz_answer2=[("X",(255,0,0),False), ("def __main__",(0,255,0),True)]

    
    def start(self,draw,image,disp):
        image.paste(self.start_img, (0,0))
        disp.image(image)
        time.sleep(0.5)
        #
        image.paste(self.back_1, (0,0))
        large = self.professor.crop((0,0,120,120))
        large = large.resize((240, 240))
        image.paste(large, (35,0),large)
        draw.rectangle((0, 145,240, 240), outline=0, fill=0) # Draw a black filled box to clear the image.
        draw.text((0, 147), "Hello, HangGong! \n Welcome to KAU \n aka.HELL \n For 4 years, \nYou can't escape!!!", font=self.fnt, fill=(255,255,255))
        disp.image(image)
        time.sleep(1)
        #
        draw.rectangle((0, 0,240, 240), outline=0, fill=(255,255,255))
        large = self.me.crop((0,0,120,120))
        large = large.resize((240, 240))
        image.paste(large, (35,0),large)
        draw.text((60, 200), "Oh, no!!!!!", font=self.fnt_big , fill=(0,0,0))
        disp.image(image)
        time.sleep(0.5)
        return image

    def walk(self,draw,image,delta_x, delta_y,backup_x,backup_y):
        state_x=1500-240+delta_x +80
        state_y=1000-240+delta_y +80
        print(state_x,state_y,self.rand_x,self.rand_y)
        

        if (self.rand_x -50< state_x and state_x< self.rand_x +50) and (self.rand_y -50< state_y and state_y< self.rand_y +50):
            self.rand_x=random.randint(0,1350)
            self.rand_y=random.randint(0,850)
            random.seed()
            self.dup = self.room.copy()
            print("meet")
            image.paste(self.room_quiz, (0,0),self.room_quiz) 
            draw.text((self.rand_x+30,self.rand_y), "!!!", font=self.fnt, fill=(255,0,0))
            su.disp.image(image)
            time.sleep(2)
            self.quiz(image,draw)

        self.dup.paste(self.professor, (self.rand_x,self.rand_y),self.professor)
        target = self.dup.crop((1500-(240-delta_x),1000-(240-delta_y),1500+delta_x,1000+delta_y)) #start from upper_point(0,430) and down_point(360,690) 


        delta_x,delta_y=utils.check_outside(target,delta_x,delta_y,backup_x,backup_y,(0,0,0)) 
        
        delta_x,delta_y=utils.check_outside(target,delta_x,delta_y,backup_x,backup_y,(255,255,255))

        image.paste(target, (0,0)) #background 
        
        return image, delta_x, delta_y
    
    def quiz(self,image,draw):
        right = False
        rand = random.randint(0,1)
        while True:
            print(rand)
            image.paste(self.back_1, (0,0))
            large = self.professor.crop((0,0,120,120))
            large = large.resize((240, 240))
            image.paste(large, (35,0),large)
            draw.rectangle((0, 145,240, 240), outline=0, fill=0) # Draw a black filled box to clear the image.
            draw.text((0, 147), self.quiz_list[rand], font=self.fnt, fill=(255,255,255))
            if not su.button_B.value:  # left pressed
                draw.rectangle((0, 190,240, 210), outline=0, fill=self.quiz_answer1[rand][1])  # up, green, yes
                right = self.quiz_answer1[rand][2]
            if not su.button_A.value:  # left pressed
                draw.rectangle((0, 210,240, 230), outline=0, fill=self.quiz_answer2[rand][1]) #down, red, no
                right = self.quiz_answer2[rand][2]
            print(right)
            
                
            draw.text((0, 190), self.quiz_answer1[rand][0], font=self.fnt, fill=(255,255,255))
            draw.text((0, 210), self.quiz_answer2[rand][0], font=self.fnt, fill=(255,255,255))
            su.disp.image(image)
            if right:
                time.sleep(0.5)
                draw.rectangle((0, 145,240, 240), outline=0, fill=0) # Draw a black filled box to clear the image.
                draw.text((0, 147), "You are right..' \n Next time will be difficult.\n you'll be wrong!!", font=self.fnt, fill=(255,255,255))
                su.disp.image(image)
                time.sleep(3)
                break


