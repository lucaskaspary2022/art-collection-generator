from typing import overload
from PIL import Image
import random
import math
import numpy as np

# y = row
# x = pixel

def calculatePixel(row, pixel):
    value = (row * 300) + pixel
    return value

def getRowandPixel(value, rows): # 555 and 255

    row = 0
    px = 0

    for i, pixel in enumerate(rows):
        if value > rows[i] and value < rows[i + 1]:
            row = i
            px = value - rows[i]

    return {'row': row, 'pixel': px}

def insertBackground(planetFile, backgroundfile, ringState):

    # stars = Image.open('./Skies/starrySky.png')
    stars = Image.open(backgroundfile)
    stars =  stars.resize((300,300), resample=Image.NEAREST)
    planet = Image.open(planetFile)
    if ringState == False:
        planet = planet.resize((140,140), resample=Image.NEAREST)
    elif ringState == True:
        planet = planet.resize((198,140), resample=Image.NEAREST)
    star1 = Image.open('./Stars/star1.png')
    star2 = Image.open('./Stars/star2.png')

    rows = []
    starsData = stars.getdata()
    bgColor = starsData[0]
    px = 0

    dimension = int(math.sqrt(len(starsData)))

    for i in range(dimension):

        if i == 0:
            rows.append(0)
        else:
            px += 300
            rows.append(px)

    star2Data = star2.getdata()
    star1Data = star1.getdata()


    x = random.randint(1, 299)
    y = random.randint(1, 299)
    # aboveX = x 
    # aboveY = y - 1

    value = calculatePixel(y,x)

    # stars.paste(star2, (x,y), star2)

    aboveValue = value - 300

    # print(rows)

    # stars.paste(star2, (aboveX, aboveY), star2)

    # for i, pixel in enumerate(starsData):
    #     if i % 300 == 0:
    #         print(i)


    # stars.paste(star2, (0,0), star2)

    data = stars.getdata()

    value = calculatePixel(0,0)

    # print(value)

    # position = calculatePixel(0,3)

    count = 0

    for i in range(40):

        white = False

        x = random.randint(5, 295)
        y = random.randint(5, 295)

        position = calculatePixel(y,x)


        for row in range(y, (y + 9) + 1):
            for pixel in range(x, 9 + 1):

                # print(f'ROW:{row} and PIXEL: {pixel}')

                value = calculatePixel(row,pixel)

                # print(value)
                # print(f'{(row,pixel)}: {data[value]}')
                count += 1

                if value > len(data):
                    break

                if data[value] == (255,255,255):
                    # print(f'bosta: {data[value]}')
                    white = True


        if white == False:
            stars.paste(star1, (x,y), star1) 


    for i in range(40):

        white = False
        outOfRange = False

        x = random.randint(2, 298)
        y = random.randint(2, 298)

        position = calculatePixel(y,x)


        for row in range(y, (y + 3) + 1):
            for pixel in range(x, 3 + 1):

                # print(f'ROW:{row} and PIXEL: {pixel}')

                value = calculatePixel(row,pixel)

                value = 90005

                if value > len(data):
                    outOfRange = True
                    break
                else:
                    outOfRange = False

                # print(value)
                # print(f'{(row,pixel)}: {data[value]}')
                count += 1

                if data[value] == (255,255,255):
                    print(f'bosta: {data[value]}')
                    white = True


        if white == False and outOfRange == False:
            stars.paste(star2, (x,y), star2) 



    # data = getRowandPixel(aboveValue, rows)
    # print(f"coordinate: {aboveValue}, row: {data['row']}, pixel: {data['pixel']}")
    # data = getRowandPixel(value, rows)
    # print(f"coordinate: {value}, row: {data['row']}, pixel: {data['pixel']}")

    # print(count)

    if ringState == False:
        stars.paste(planet, (75,75), planet)
    elif ringState == True:
        stars.paste(planet, (50,75), planet)

    resized_img = stars.resize((300, 300), resample=Image.NEAREST)
    resized_img.save(planetFile)