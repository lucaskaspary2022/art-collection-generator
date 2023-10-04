from PIL import Image 

# changes land color to whatever color I set

planet = Image.open('earth.png')
planet = planet.convert("RGBA")

data = planet.getdata()

newData = []
newColor = (int(139* 3/4),int(195* 3/4),int(74 * 3/4))
# ovo = (255,255,255)

for i, pixel in enumerate(data):
    # print(pixel)
    if pixel[0] == 139 and pixel[1] == 195 and pixel[2] == 74:
        newData.append(newColor)
    else:
        newData.append(pixel)

planet.putdata(newData)
planet.save('newLand.png', 'PNG')