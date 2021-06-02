import time
from PIL import Image, ImageDraw, ImageFont




# Create the display

class Game1:
    def __init__(self):
        self.start_img = Image.open('/home/pi/Embedded/embedded_game/img/Game1/Game1_start.png')
        self.professor = Image.open('/home/pi/Embedded/embedded_game/img/Game1/pro.png')
        self.back_1 = Image.open('/home/pi/Embedded/embedded_game/img/Game1/Map3_G1.png')
        # self.image = Image.new("RGBA", (self.width, self.height))
        # self.draw = ImageDraw.Draw(self.image)
        # Clear display.


        # self.fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
        # # image 
        # self.background = Image.open('/home/pi/Embedded/embedded_game/img/HangPark.png')
        # self.me = Image.open('/home/pi/Embedded/embedded_game/img/Me2.png')

    
    def start(self, image,disp):
        image.paste(self.start_img, (0,0))
        disp.image(image)
        time.sleep(1)
        image.paste(self.back_1, (0,0))
        large = self.professor.crop((80,100,220,240))
        large = large.resize((240, 240))
        image.paste(large, (35,0),large)
        disp.image(image)
        time.sleep(1)
        return image
    def game(self, image):
        
        image.paste(self.professor, (0,0),self.professor)
        return image    
            # #draw.rectangle((0, 0, width, height), outline=0, fill=0) # Draw a black filled box to clear the image.
            # if not self.button_U.value:  # up pressed
            #     self.delta_y-=20
            # if not self.button_D.value:  # down pressed
            #     self.delta_y +=20
            # if not self.button_L.value:  # left pressed
            #     self.delta_x-=20
            # if not self.button_R.value:  # right pressed
            #     self.delta_x+=20
            # if not self.button_C.value:  # center pressed
            #     pass

            # if not self.button_A.value:  # left pressed
            #     pass
            # if not self.button_B.value:  # left pressed
            #     pass

            # if (120+self.delta_x)>240 and (0+self.delta_y) >240:
            #     self.delta_x=0
            #     self.delta_y=0
            #     break
            
                
            # self.image.paste(self.me, (120+self.delta_x, 0+self.delta_y ),self.me)

            # #print((0+delta_x,430+delta_y,360+delta_x,690+delta_y))

            
                
            
            # #Character.move(delta_x, delta_y)
            
            # #draw.ellipse((85+delta_x,85+delta_y,150+delta_x,150+delta_y), fill="#FFFFFF")

            # # Display the Image
            # self.disp.image(self.image)

            # time.sleep(0.01)
                