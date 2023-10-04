from PIL import Image
import numpy as np

bg = (255,255,255,1)

image = []

for row in range(24):
    x = []
    for pixel in range(34):
        x.append(bg)

    image.append(x)

avatar_array = np.array(image, dtype=np.uint8)
avatar_image = Image.fromarray(avatar_array)
avatar_image.save("noBackground.png")