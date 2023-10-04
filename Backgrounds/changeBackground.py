from PIL import Image

backgrounds = {"purple": [(10,5,35)], "red": [(19,3,8), (45,9,20)], "green": [(3,21,18), (5,47,28)], "blue": [(5,8,26)], 
                "dark purple":[(12,3,27)], "black": [(6,1,19)], "blue green": [(0, 20, 15)], "red purple": [(20,5,20)]}

file = 'testBackground.png' # 100px

image = Image.open(file)
img = image.convert('RGBA')

data = img.getdata()

count = 0
darkColor = backgrounds["red purple"][0]
lightColor = (int(darkColor[0] * 1.5), int(darkColor[1] * 1.5), int(darkColor[2] * 1.5))

newData = []

for pixel in data:
    # print(pixel) 
    if pixel == (0,0,0,255):
        newColor = backgrounds["red purple"][0]
        newData.append(newColor)

    elif pixel == (255,255,255,255):
        newColor = lightColor
        newData.append(newColor)
    else:
        newData.append(pixel)
    # newData.append((int(pixel[0] * 3/4), int(pixel[1] * 3/4), int(pixel[2] * 3/4)))
        

img.putdata(newData)
img.save('newSpace6.png', 'PNG')

