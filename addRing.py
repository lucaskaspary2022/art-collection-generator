from PIL import Image

# colors = [(181,181,181),(230,230,230)]

#  (255, 87, 34) and (255, 193, 7)

def insertRing(planetFile, colors):

    noBackground = Image.open('noBackground.png')
    planet = Image.open(planetFile)
    noBackground.paste(planet, (5,0), planet)
    noBackground.save('ajustedToRing.png')

    newPlanet = Image.open('ajustedToRing.png')
    ring = Image.open('./Rings/ring1.png')

    data = ring.getdata()

    newData = []

    for i, pixel in enumerate(data):
        if pixel[0] == 255 and pixel[1] == 87 and pixel[2] == 34:
            newData.append(colors[0])
        elif pixel[0] == 255 and pixel[1] == 193 and pixel[2] == 7:
            newData.append(colors[1])
        else:
            newData.append(pixel)

    ring.putdata(newData)
    # ring.save('newRing.png', 'PNG')

    newPlanet.paste(ring, (0,0), ring)

    newPlanet.save(planetFile)

    return True