from PIL import Image
import numpy as np
from convert import removeBackground

# images 24x24 => only planets without background 

# create a small array of different backgrounds for all images
# crate the planets
# create program to overlap them
# maybe create a file just for the border and then overlap
# create function to getRing and to getPlanet
# create many different planet models and base new planets on a big array of crated planets

def generatePlanet(color, file):

    bd = (0,0,0)
    # fl = (48, 114, 230)
    # fl = (229,60,160)
    # fl = (0,150,136)
    bg = (255,255,255)
    # bg = (12,20,56)
    # green = (58,180,75)

    # 5x5

    pixels_list = []

    for row in range(24):
        x = []
        for pixel in range(24):  # 8 9 10 11 12 13 14 15

            if row == 0 or row == 23:
                if pixel < 8 or pixel > 15:
                    x.append(bg)
                else:
                    x.append(bd)

            elif row == 1 or row == 22:
                if (pixel > 5 and pixel < 8) or (pixel > 15 and pixel < 18):
                    x.append(bd)
                elif pixel < 6 or pixel > 17:
                    x.append(bg)
                else:
                    x.append(color)

            elif row == 2 or row == 21:
                if pixel == 5 or pixel == 18:
                    x.append(bd)
                elif pixel < 5 or pixel > 18:
                    x.append(bg)
                else:
                    x.append(color)

            elif row == 3 or row == 20:
                if pixel == 4 or pixel == 19:
                    x.append(bd)
                elif pixel < 4 or pixel > 19:
                    x.append(bg)
                else:
                    x.append(color)

            elif row == 4 or row == 19:
                if pixel == 3 or pixel == 20:
                    x.append(bd)
                elif pixel < 3 or pixel > 20:
                    x.append(bg)
                else:
                    x.append(color)

            elif row == 5 or row == 18:
                if pixel == 2 or pixel == 21:
                    x.append(bd)
                elif pixel < 2 or pixel > 21:
                    x.append(bg)
                else:
                    x.append(color)

            elif (row > 5 and row < 8) or (row > 15 and row < 18):
                if pixel == 1 or pixel == 22:
                    x.append(bd)
                elif pixel < 1 or pixel > 22:
                    x.append(bg)
                else:
                    x.append(color)

            elif row > 7 and row < 16:
                if pixel == 0 or pixel == 23:
                    x.append(bd)
                else:
                    x.append(color)

            # else:
            #     x.append(green)

        pixels_list.append(x)
        

    planet_array = np.array(pixels_list, dtype=np.uint8)
    planet_image = Image.fromarray(planet_array)
    # avatar_image = avatar_image.resize((300, 300), resample=Image.NEAREST)
    planet_image = removeBackground(planet_image)
    # file = './Planets/newPlanet3.png'
    planet_image.save(file)
    

    return file

    # width, height = Image.open('exotic.png').size