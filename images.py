from PIL import Image, ImageDraw, ImageFont


#font 
fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
fnt_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
fnt_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)

#



#Backgrounds 
opening = Image.open('/home/pi/Embedded/embedded_game/img/opening.png')
back = [Image.open('/home/pi/Embedded/embedded_game/img/Map3.png'), Image.open('/home/pi/Embedded/embedded_game/img/HangPark.png'), Image.open('/home/pi/Embedded/embedded_game/img/Game2/soccer.png')]
#[0]: main, [1]:game1, [2]: game2


#Game1 
start_img = Image.open('/home/pi/Embedded/embedded_game/img/Game1/Game1_start.png')
back_1 = Image.open('/home/pi/Embedded/embedded_game/img/Game1/Map3_G1.png')
me = Image.open('/home/pi/Embedded/embedded_game/img/Me3.png')
room = Image.open('/home/pi/Embedded/embedded_game/img/Game1/Game1_room2.png')
room_quiz = Image.open('/home/pi/Embedded/embedded_game/img/Game1/Quiz.png')
end_1 = Image.open('/home/pi/Embedded/embedded_game/img/Game1/1_End.png')
return_1 = Image.open('/home/pi/Embedded/embedded_game/img/Game1/1_Return.png')


#people 
pro_kill = Image.open('/home/pi/Embedded/embedded_game/img/Game1/pro1.png')
# large = me.crop((0,0,120,120))
#large = large.resize((150, 150))

#Game2
me2 = Image.open('/home/pi/Embedded/embedded_game/img/Game2/me_2.png')
me2_leg= Image.open('/home/pi/Embedded/embedded_game/img/Game2/me_2_leg.png')
ball = Image.open('/home/pi/Embedded/embedded_game/img/Game2/ball.png')

#Graduation
graduate = Image.open('/home/pi/Embedded/embedded_game/img/Graduation/gradutate.png')
company = Image.open('/home/pi/Embedded/embedded_game/img/Graduation/company.png')
me_g= Image.open('/home/pi/Embedded/embedded_game/img/Graduation/me_G.png')
me_em = Image.open('/home/pi/Embedded/embedded_game/img/Graduation/me_em.png')
employed = Image.open('/home/pi/Embedded/embedded_game/img/Graduation/employed.png')
passed = Image.open('/home/pi/Embedded/embedded_game/img/Graduation/pass.png')


