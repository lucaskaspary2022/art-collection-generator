from PIL import Image
import random

def calculatePixel(row, pixel):
    value = (row * 24) + pixel
    return value

lighGrey = (158, 158, 158, 255)
darkGrey = ''

shadows = [ [1,8,15], [2,6], [3,5], [4,4], [5,3,4], [6,3,2], [7,3,2], [8,22,3,2,1], [9,3,2,1], 
            [10,3,2,1], [11,3,2,1], [12,3,2,1], [13,4,3,2,1], [14,4,3,2,1], [15,22,5,4,3,2,1], 
            [16,6,5,4,3,2,1], [17,21,7,6,5,4,3,2], [18,20,8,7,6,5,4,3], [19,19,18,10,9,8,7,6,5,4],
            [20,18,17,16,15,14,13,12,11,10,9,8,7,6,5], [21,17,16,15,14,13,12,11,10,9,8,7,6],
            [22,15,14,13,12,11,10,9,8]
        ]

def insertCrater(planetFile, craterFile):

    # print(planetFile)

    planet = Image.open(planetFile)
    # planet  = Image.open('darker.png')
    planetData = planet.getdata()

    # print(planetData)

    craters = []
    used = []

    # for i in range(4):
    # num = random.randint(1,24)
    # craterFile = f'./Craters/craters{1}.png'
    # craterFile = './Craters/craters1.png'

        # while craterFile in used:
        #     num = random.randint(1,24)
        #     craterFile = f'./Craters/crater{num}.png'

    crater = Image.open(craterFile)
    # crater = Image.open('./Craters/newCrater.png')

    # planet.paste(crater, (0,0), crater)
        
    # planet.save(planetFile, 'PNG')
    # return

    newData = []
    # craterPlanetData = planet.getdata()
    craterData = crater.getdata()

    shadowPixels = []
    shadowModify = []

    for duo in shadows:
        if len(duo) > 2:
            for j in range(1,len(duo)):
                shadowPixel = calculatePixel(duo[0], duo[j])
                shadowPixels.append(shadowPixel)
        else:
            shadowPixel = calculatePixel(duo[0], duo[1])
            shadowPixels.append(shadowPixel)

    for i, pixel in enumerate(craterData):
        if pixel == (158, 158, 158, 255):
            if i in shadowPixels:
                shadowModify.append((97,97,97,255))
            else:
                shadowModify.append(pixel)
        else:
            shadowModify.append(pixel)


    for i, pixel in enumerate(shadowModify):
        if pixel == (158, 158, 158, 255):
            color = planetData[i]
            newColor = (int(color[0] * 3/4),int(color[1] * 3/4),int(color[2] * 3/4))
            newData.append(newColor)

        elif pixel == (33, 33, 33, 255):
            color = planetData[i]
            newColor = (int(color[0] * 2/4),int(color[1] * 2/4),int(color[2] * 2/4))
            newData.append(newColor)

        elif pixel == (97,97,97,255):
            color = planetData[i]
            newColor = (int(color[0] * 3/4),int(color[1] * 3/4),int(color[2] * 3/4))
            newData.append(newColor)

        else:
            newData.append(pixel)

    # for i, pixel in enumerate(craterData):
    #     if pixel == (158, 158, 158, 255):

    #         # print(i)

    #         shadowModify = []

    #         for duo in shadows:
    #             if len(duo) > 2:
    #                 for j in range(1,len(duo)):
    #                     shadowPixel = calculatePixel(duo[0], duo[j])
    #                     shadowModify.append(shadowPixel)
    #             else:
    #                 shadowPixel = calculatePixel(duo[0], duo[1])
    #                 shadowModify.append(shadowPixel)


    #         if i in shadowModify:
    #             newColor = (int(planetData[shadowModify[0]][0] * 3/4),int(planetData[shadowModify[0]][1] * 3/4),int(planetData[shadowModify[0]][2] * 3/4))
    #             newData.append(newColor)
    #         else:
    #             newData.append(planetData[shadowModify[0]])

    #     elif pixel == (33, 33, 33, 255):

    #         shadowModify = []

    #         for duo in shadows:
    #             if len(duo) > 2:
    #                 for j in range(1,len(duo)):
    #                     shadowPixel = calculatePixel(duo[0], duo[j])
    #                     shadowModify.append(shadowPixel)
    #             else:
    #                 shadowPixel = calculatePixel(duo[0], duo[1])
    #                 shadowModify.append(shadowPixel)

    #         newColor = (int(planetData[shadowModify[0]][0] * 3/4),int(planetData[shadowModify[0]][1] * 3/4),int(planetData[shadowModify[0]][2] * 3/4))
    #         newData.append(newColor)

    #     else:
    #         newData.append(pixel)

    crater.putdata(newData)

    planet.paste(crater, (0,0), crater)
    planet.save(planetFile, 'PNG')
    # planet.save('./Craters/craterPlanet1.png')

# num = random.randint(1,24)
# craterFile = f'./Craters/crater{num}.png'
# crater = Image.open(craterFile)

# planet.paste(crater, (0,0), crater)

# planet.save('./Planets/craterPlanet.png')

    
    