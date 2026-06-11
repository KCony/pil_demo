from PIL import Image, ImageDraw
import util
import sys
sys.path.append(r'..')
import zip_util

im = Image.new(mode="RGB", size=(500, 500))
#im.show()
draw = ImageDraw.Draw(im)
#draw.text((10, 10), "Hello World!")
#draw.line(xy=(0, 20, 499, 20), fill=(255, 255, 0), width=10)
#draw.line(xy=(20, 0, 20, 499), fill=(160, 160, 0), width=10)
draw.line(xy=(0, 20, 499, 20), fill=(255, 255, 255), width=2)
draw.line(xy=(0, 30, 499, 30), fill=(255, 255, 255), width=2)
draw.line(xy=(0, 40, 499, 40), fill=(255, 255, 255), width=2)
draw.line(xy=(20, 0, 20, 499), fill=(255, 255, 255), width=2)
draw.line(xy=(30, 0, 30, 499), fill=(255, 255, 255), width=2)
#im.show()

# TODO: Write a loop to draw all live cells

draw.rectangle(xy=(22, 32, 29, 39), fill=(0,60,0), outline=(0,60,0))
draw.rectangle(xy=(244, 244, 254, 254), fill="green", outline="green")
im.save('grid.png')
print(util.comp())
print(zip_util.read_zip_all(r'..\zip_codes_states.csv')[0])
