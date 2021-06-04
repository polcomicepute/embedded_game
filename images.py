from PIL import Image, ImageDraw, ImageFont


#font 
fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
fnt_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)



#Backgrounds 
back = [Image.open('/home/pi/Embedded/embedded_game/img/Map3.png'), Image.open('/home/pi/Embedded/embedded_game/img/HangPark.png')]
#[0]: main, [1]:game1 


#Game1 
start_img = Image.open('/home/pi/Embedded/embedded_game/img/Game1/Game1_start.png')
back_1 = Image.open('/home/pi/Embedded/embedded_game/img/Game1/Map3_G1.png')
me = Image.open('/home/pi/Embedded/embedded_game/img/Me3.png')
room = Image.open('/home/pi/Embedded/embedded_game/img/Game1/Game1_room2.png')
room_quiz = Image.open('/home/pi/Embedded/embedded_game/img/Game1/Quiz.png')
end_1 = Image.open('/home/pi/Embedded/embedded_game/img/Game1/1_End.png')
return_1 = Image.open('/home/pi/Embedded/embedded_game/img/Game1/1_Return.png')


#people 
me = Image.open('/home/pi/Embedded/embedded_game/img/Me3.png')
pro_kill = Image.open('/home/pi/Embedded/embedded_game/img/Game1/pro1.png')
