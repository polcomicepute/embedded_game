import time
import random
from colorsys import hsv_to_rgb
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Create the display
cs_pin = DigitalInOut(board.CE0)
dc_pin = DigitalInOut(board.D25)
reset_pin = DigitalInOut(board.D24)
BAUDRATE = 24000000

spi = board.SPI()
disp = st7789.ST7789(
    spi,
    height=240,
    y_offset=80,
    rotation=180,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
)

# Input pins:
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT

# Turn on the Backlight
backlight = DigitalInOut(board.D26)
backlight.switch_to_output()
backlight.value = True

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for color.
width = disp.width
height = disp.height
image = Image.new("RGBA", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Clear display.
draw.rectangle((0, 0, width, height), outline=0, fill=(255, 0, 0))
disp.image(image)

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

udlr_fill = "#00FF00"
udlr_outline = "#00FFFF"
button_fill = "#FF00FF"
button_outline = "#FFFFFF"

BULLET_UP= []
BULLET_DOWN=[]
bullet_up=0
bullet_down=0

state_y=0
state_x=0

fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
# image 
background = Image.open('./img/HangPark.png')
me = Image.open('./img/Me.png')
hangmap =  Image.open('./img/Map.png')


while True:

    # Draw a black filled box to clear the image.
    image.paste(background, (0,0))
    
    #draw.rectangle((0, 0, width, height), outline=0, fill=0)

    up_fill = 0
    if not button_U.value:  # up pressed
        up_fill = udlr_fill
        state_y-=1
    #draw.polygon(
    #    [(40, 40), (60, 4), (80, 40)], outline=udlr_outline, fill=up_fill
    #)  # Up

    down_fill = 0
    if not button_D.value:  # down pressed
        down_fill = udlr_fill
        state_y +=1
    #draw.polygon(
    #    [(60, 120), (80, 84), (40, 84)], outline=udlr_outline, fill=down_fill
    #)  # down

    left_fill = 0
    if not button_L.value:  # left pressed
        left_fill = udlr_fill
        state_x-=1
    #draw.polygon(
    #    [(0, 60), (36, 42), (36, 81)], outline=udlr_outline, fill=left_fill
    #)  # left

    right_fill = 0
    if not button_R.value:  # right pressed
        right_fill = udlr_fill
        state_x+=1
    #draw.polygon(
    #    [(120, 60), (84, 42), (84, 82)], outline=udlr_outline, fill=right_fill
    #)  # right

    center_fill = 0
    if not button_C.value:  # center pressed
        center_fill = button_fill
    #draw.rectangle((40, 44, 80, 80), outline=button_outline, fill=center_fill)  # center

    A_fill = 0
    if not button_A.value:  # left pressed
        A_fill = button_fill
        BULLET_DOWN.append([True, 0])
    #draw.ellipse((140, 80, 180, 120), outline=button_outline, fill=A_fill)  # A button

    B_fill = 0
    if not button_B.value:  # left pressed
        B_fill = button_fill
        BULLET_UP.append([True, 0])
    #draw.ellipse((190, 40, 230, 80), outline=button_outline, fill=B_fill)  # B button
    for i in BULLET_DOWN:
        if i[0]:
            if 120+state_y+i[1] <height:
                draw.ellipse((100+state_x,100+state_y+i[1],120+state_x,120+state_y+i[1]), fill=udlr_fill)
                i[1]= i[1]+8
            else:
                BULLET_DOWN.remove(i)
    for j in BULLET_UP:
        if j[0]:
            if 120+state_y+j[1] >0:
                draw.ellipse((100+state_x,100+state_y+j[1],120+state_x,120+state_y+j[1]), fill=button_fill)
                j[1]= j[1]-8
            else:
                BULLET_UP.remove(j)
    image.paste(me, (state_x,state_y),me)


    #draw.ellipse((85+state_x,85+state_y,150+state_x,150+state_y), fill="#FFFFFF")

    # Display the Image
    disp.image(image)

    time.sleep(0.01)
