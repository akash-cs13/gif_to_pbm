import os
import board
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw

path = os.path.dirname(__file__) + '/'

oled_reset = digitalio.DigitalInOut(board.D4)
WIDTH = 128
HEIGHT = 64

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3c, reset=oled_reset)
oled.fill(0)
oled.show()

width = oled.width
height = oled.height

image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=0)

def animation(animation_name, total_frames=25):
    for x in range(1, total_frames):
        image = Image.open(path + f'{animation_name}/frame('+str(x)+').pbm').convert('1')
        oled.image(image)
        oled.show()

animation("Animation")
draw.rectangle((0, 0, width, height), outline=0, fill=0)
oled.image(image)
oled.show()