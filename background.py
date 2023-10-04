from PIL import Image
import numpy as np

bg = (int(19 * 1/2),int(0 * 1),int(51 * 1/2))
bg = (15,10,28) # RGB

image = []

# size = 2000
size = 300

for row in range(size):
    x = []
    for pixel in range(size):
        x.append(bg)

    image.append(x)

avatar_array = np.array(image, dtype=np.uint8)
avatar_image = Image.fromarray(avatar_array)
avatar_image.save("./Backgrounds/background4.png")