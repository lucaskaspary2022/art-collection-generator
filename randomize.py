import random
from test import generatePlanet
from insertLines import addSurface
from shadow import addShadow
from addRing import insertRing
from addBackground import insertBackground
from Metadata import metadata
import json
from nftColors import colorsList

files = {
    1: './Lands/land1.png',
    2: './Lands/land2.png',
    3: './Lands/land3.png',
    4: './Lands/land4.png',
    5: './Lands/land5.png',
    6: './Lines/lines1.png',
    7: './Lines/lines2.png',
    8: './Lines/lines3.png'
}

surfaces = {
    1: './Lands/land',
    2: './Lines/lines',
    3: './Craters/crater'
}

planetColorsUsed = []

for i in range(10):
    ringColors = [[(181,181,181),(230,230,230)]]

    ring = False

    # Flat planets
    # Crater planets
    # Land planets
    # Striped planets

    surfaceFile = ''

    planetMetadata = {
        "name": "",
        "desciption": "Just not even 0.1 percent of our universe",
        "atributes": [
            {
                "trait_type": "Galaxy",
                "value": ""
            },
            {
                "trait_type": "color",
                "value": ""
            },
            {
                "trait_type": "size",
                "value": ""
            }
        ]
    }

    planetNumber = random.randint(0,135)
    surfaceNumber = random.randint(0,135)

    planetColor = colorsList[planetNumber]
    landColor = colorsList[surfaceNumber]

    planetFile = f'Planets/planet{i}.png'

    # if color already used:

    duplicated = False

    while duplicated == False:
        for item in planetColorsUsed:
            if item['planet'] == planetColor:
                print(f"shit, {planetColor} is the same as {item['planet']}")
                duplicated = True
                break

        break

    planet = generatePlanet(planetColor, planetFile)

    if i % 2 == 0:    
        surfaceNum = random.randint(1,3)
        surfaceType = surfaces[surfaceNum]

        if 'Lands' in surfaceType:
            landID = random.randint(1,5)
            surfaceFile = f'{surfaceType}{landID}.png'
        elif 'Lines' in surfaceType:
            lineID = random.randint(1,3)
            surfaceFile = f'{surfaceType}{lineID}.png'

        # elif 'Craters' in surfaceFile:
            
        # planetColorsUsed['planet'] = planetColor

        planetColorsUsed.append({
            'planet': planetColor,
            'surface': {
                'file': surfaceFile,
                'color': landColor
            }
        })

        # planetColorsUsed['surface'] = {
        #     'file': surfaceFile,
        #     'color': landColor
        # }
        
        if surfaceFile:
            addSurface(planet, surfaceFile)
    else: 

        planetColorsUsed.append({
            'planet': planetColor,
            'surface': ''
        })


        # while planetColor in planetColorsUsed:
        #     pr = random.randint(0,255)
        #     pg = random.randint(0,255)
        #     pb = random.randint(0,255)

        #     planetColor = (pr,pg,pb)
    

    addShadow(planet)

    ringState = random.randint(1,5)

    if ringState % 3 == 0:
        ring = insertRing(planet, ringColors[0])

    insertBackground(planet, './Backgrounds/background2.png', ring)

    jsonFile = f'./Metadata/planet{i}.json'

    planetMetadata["name"] = f"Planet {i}"
    planetMetadata["atributes"][0]["value"] = f"Galaxy {i}000"
    planetMetadata["atributes"][1]["value"] = planetColor
    planetMetadata["atributes"][2]["value"] = random.randint(100,100000)

    if surfaceFile:
        if 'Lands' in surfaceFile:
            planetMetadata["atributes"].append({
                "trait_type": "Surface",
                "value": "Land"
            })
        elif 'Lines' in surfaceFile:
            planetMetadata["atributes"].append({
                "trait_type": "Surface",
                "value": "Stripes" 
            })

    with open(jsonFile, 'w') as file:
        json.dump(planetMetadata, file)


    # planetColorsUsed.append({
    #     'planet': planetColor,
    #     f'{surfaceFile}': landColor
    # })


    # if backgroundImage is './Backgrounds/background2.png':
        # add galaxy name to planet metadata and create json file

    # craate algorithim to pick whether the planet is going to have craters, stripes or land

    # keep track of the color combinations to avoid repetitive ones

# print(planetColorsUsed)

# for i, item in enumerate(planetColorsUsed):
#     print(f'{i}: {item}')