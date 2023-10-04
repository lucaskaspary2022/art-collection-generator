from PIL import Image
import random
import numpy as np

colors = []

for i in range(3):
    number = random.randint(0, 60)
    colors.append(number)

print(colors)

image = []
bg = (colors[0],colors[1],colors[2])

for row in range(300):
    x = []
    for pixel in range(300):
        x.append(bg)

    image.append(x)

avatar_array = np.array(image, dtype=np.uint8)
avatar_image = Image.fromarray(avatar_array)
avatar_image.save("background5.png")