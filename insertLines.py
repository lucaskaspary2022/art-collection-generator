from PIL import Image

def changeStripe(color, data):
    newData = []
    for i, pixel in enumerate(data):
        if pixel[3] != 0:
            newData.append(color)
        else:
            newData.append(pixel)

    return newData

def addSurface(planetFile, surfaceFile, surfaceColor):

    # planetFile = 'darker.png'
    # surfaceFile = './Lines/lines4.png'
    # surfaceColor = (29,191,115)

    planet = Image.open(planetFile)

    lines = Image.open(surfaceFile)
    # lines = Image.open('./Lands/land2.png')

    data = lines.getdata()

    newLines = changeStripe(surfaceColor, data)
    lines.putdata(newLines)
    # lines.save('newStripes.png', 'PNG')

    planet.paste(lines, (0,0), lines)

    planet.save(planetFile)