from PIL import Image

def addShadow(planetFile):

    def calculatePixel(row, pixel):
        value = (row * 24) + pixel
        return value

    shadows = [ [1,8,15], [2,6], [3,5], [4,4], [5,3,4], [6,3,2], [7,3,2], [8,22,3,2,1], [9,3,2,1], 
                [10,3,2,1], [11,3,2,1], [12,3,2,1], [13,4,3,2,1], [14,4,3,2,1], [15,22,5,4,3,2,1], 
                [16,6,5,4,3,2,1], [17,21,7,6,5,4,3,2], [18,20,8,7,6,5,4,3], [19,19,18,10,9,8,7,6,5,4],
                [20,18,17,16,15,14,13,12,11,10,9,8,7,6,5], [21,17,16,15,14,13,12,11,10,9,8,7,6],
                [22,15,14,13,12,11,10,9,8]
            ]

    planet = Image.open(planetFile)
    # planet = Image.open('earth.png')

    planet = planet.convert("RGBA")

    data = planet.getdata()

    newData = []

    pixel = calculatePixel(1,8)

    pixelList = []

    for duo in shadows:
        if len(duo) > 2:
            for i in range(1,len(duo)):
                newPixel = calculatePixel(duo[0], duo[i])
                pixelList.append(newPixel)
        else:
            newPixel = calculatePixel(duo[0], duo[1])
            pixelList.append(newPixel)

    for i, pixel in enumerate(data):
        if i in pixelList:
            # newData.append((27,82,177))
            newData.append((int(pixel[0] * 3/4), int(pixel[1] * 3/4), int(pixel[2] * 3/4)))
        else:
            newData.append(pixel)

    planet.putdata(newData)
    planet.save(planetFile, 'PNG')
    planet.save('darker.png', 'PNG')