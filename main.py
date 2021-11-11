from PIL import Image

from PIL import ImageFont
from PIL import ImageDraw

import os
import random

# SETTINGS

generate_images = False
generate_data_file = True

shuffle_lines_in_file = True

# GENERATE IMAGES

fonts = os.listdir("fonts/")

if not os.path.exists("data"):
    os.makedirs("data")

filename = "train.data"

fp = open(filename, "w")

for i in range(1, 10):
    num = 1
    if not os.path.exists("data/" + str(i)):
        os.makedirs("data/" + str(i))
    for font in fonts:
        img = Image.new('RGB', (28, 28))
        draw = ImageDraw.Draw(img)
        loadedFont = ImageFont.truetype("fonts/" + font, random.randint(16, 22))
        draw.text((8,0), str(i), (255, 255, 255), font=loadedFont)
        if generate_data_file:
            fp.write(str(i) + "#")
            pixels = img.load()
            for l in range(img.size[0]):
                for m in range(img.size[1]):
                    if pixels[m, l][0] > 255/2:
                        fp.write("1")
                    else:
                        fp.write("0")
            fp.write("\n")
        if generate_images:
            img.save("data/" + str(i) + "/" + str(num) + ".jpg")
        num += 1

fp.close()

# SHUFFLE

if shuffle_lines_in_file:
    lines = open(filename).readlines()
    random.shuffle(lines)
    open(filename, "w").writelines(lines)
