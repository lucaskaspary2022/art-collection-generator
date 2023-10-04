from os import dup
import random

from async_timeout import enum
from test import generatePlanet
from insertLines import addSurface
from shadow import addShadow
from addRing import insertRing
from addBackground import insertBackground
import json
from nftColors import colorsList
from addCrater import insertCrater
from fixSinglePlanet import improveResolution

# def checkRepeatedColor(planetColorsUsed, planetColor, landColor):


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
    2: './Lines/lines'
    # 3: './Craters/craters'
}

craterOrFlat = {
    1: '',
    2: './Craters/craters'
}

galaxies = {
    1: './Backgrounds/background1.png',
    2: './Backgrounds/background2.png',
    3: './Backgrounds/background3.png',
    4: './Backgrounds/background5.png',
    5: './Backgrounds/background5.png',
    6: './Backgrounds/background6.png',
    7: './Backgrounds/background7.png',
}

# galaxies = {
#     1: './Backgrounds/newSpace1.png',
#     2: './Backgrounds/newSpace2.png',
#     3: './Backgrounds/newSpace3.png',
#     4: './Backgrounds/newSpace4.png',
#     5: './Backgrounds/newSpace5.png',
#     6: './Backgrounds/newSpace6.png'
# }

galaxyNames = {
    1: 'Andromeda',
    2: 'Malin 1',
    3: 'Centaurus A',
    4: 'Circinus',
    5: 'Cosmos Redshift 7',
    6: 'Sunflower Galaxy',
    7: 'Milky Way'
}

planetColorsUsed = []

for i in range(1,9001):
    ringColors = [[(181,181,181),(230,230,230)], [(136,43,226), (153,102,204)], [(6,146,208), (64,224,208)], [(183,115,51), (179,139,109)], [(255,223,0), (255,243,78)], [(64,224,208), (127,255,211)], [(248,131,120), (247,184,159)], [(255,165,0), (255,199,119)], [(217,216,215), (245,245,245)]]

    ring = False

    # Flat planets
    # Crater planets
    # Land planets
    # Striped planets

    surfaceFile = ''

    planetMetadata = {
        "name": "",
        "description": "Not even just 0.0000000000000001 percent of our universe",
        "attributes": [
            {
                "trait_type": "Galaxy",
                "value": ""
            },
            {
                "trait_type": "Color",
                "value": ""
            },
            {
                "trait_type": "Surface",
                "value": ""
            },
            {
                "trait_type": "Size (Diameter)",
                "value": ""
            },
            {
                "trait_type": "Ring",
                "value": ""
            }
        ]
    }

    # planetNumber = random.randint(0,134)
    # surfaceNumber = random.randint(0,134)
    planetNumber = random.randint(0,134)
    surfaceNumber = random.randint(0,134)

    while planetNumber == surfaceNumber:
        planetNumber = random.randint(0,134)
        surfaceNumber = random.randint(0,134)

    if planetNumber == surfaceNumber:
        break

    planetColor = colorsList[planetNumber][0]
    landColor = colorsList[surfaceNumber][0]

    planetFile = f'Planets/{i}.png'
    # planetFile = f'PlanetsTest/planet{i}.png'

    planet = generatePlanet(planetColor, planetFile)

    if i % 2 == 0:    
        surfaceNum = random.randint(1,2)
        surfaceType = surfaces[surfaceNum]

        if 'Lands' in surfaceType:
            landID = random.randint(1,5)
            surfaceFile = f'{surfaceType}{landID}.png'
        elif 'Lines' in surfaceType:
            lineID = random.randint(1,3)
            surfaceFile = f'{surfaceType}{lineID}.png'

        duplicatedSurfacePlanet = False
            
        for item in planetColorsUsed:
            if item['surface']:
                # print(f"{item['surface']}")
                if (item['surface']['file'] == surfaceFile and item['surface']['color'] == landColor) and item['planet'] == planetColor:
                    # print(f"File '{item['surface']['file']}' is the same as '{surfaceFile}' and Color '{item['surface']['color']} is the same as '{landColor}'")
                    duplicatedSurfacePlanet = True
                    break

        while duplicatedSurfacePlanet == True:

            # print('in here')

            duplicatedSurfacePlanet = False
            # planetNumber = random.randint(0,134)
            planetNumber = random.randint(0,134) # chooses the color of the planet
            surfaceNumber = random.randint(0,134) # chooses the color of the surface

            while planetNumber == surfaceNumber:
                planetNumber = random.randint(0,134)
                surfaceNumber = random.randint(0,134)

            planetColor = colorsList[planetNumber][0]
            landColor = colorsList[surfaceNumber][0]

            surfaceNum = random.randint(1,2)
            surfaceType = surfaces[surfaceNum]

            if 'Lands' in surfaceType:
                landID = random.randint(1,5)
                surfaceFile = f'{surfaceType}{landID}.png'
            elif 'Lines' in surfaceType:
                lineID = random.randint(1,3)
                surfaceFile = f'{surfaceType}{lineID}.png'

            # elif 'Craters' in surfaceType:
            #     craterID = 1
            #     surfaceFile = f'{surfaceType}{craterID}.png'

            for item in planetColorsUsed:
                if item['surface']:
                    if (item['surface']['file'] == surfaceFile and item['surface']['color'] == landColor) and item['planet'] == planetColor:
                        # print(f"File '{item['surface']['file']}' is the same as '{surfaceFile}' and Color '{item['surface']['color']} is the same as '{landColor}'")
                        duplicatedSurfacePlanet = True
                        break    

            if duplicatedSurfacePlanet == False:
                break

        planetColorsUsed.append({
            'planet': planetColor,
            'surface': {
                'file': surfaceFile,
                'color': landColor
            }
        })
        
        if surfaceFile:
            planet = generatePlanet(planetColor, planetFile)
            addSurface(planet, surfaceFile, landColor)
            # print(f"{i}: surface")
    else: 

        choice = random.randint(1,2)

        fileType = craterOrFlat[choice]

        if 'Craters' in fileType:

            craterID = random.randint(1,6)
            craterFile = f'./Craters/craters{craterID}.png'

            duplicatedCrater = False

            for j, item in enumerate(planetColorsUsed):
                if item['surface']:
                    if 'Craters' in item['surface']['file'] and item['planet'] == planetColor: # checks if planet color already has any type of crater
                        # print(f"({i}) File '{item['surface']['file']}' is the same as ({j + 1}) '{craterFile}' and Color '{item['planet']} is the same as '{planetColor}'")
                        # duplicatedSurfacePlanet = True
                        duplicatedCrater = True
                        break

            while duplicatedCrater == True:

                duplicatedCrater = False
                # planetNumber = random.randint(0,134)
                planetNumber = random.randint(0,134)
                planetColor = colorsList[planetNumber][0]

                craterID = random.randint(1,6)
                craterFile = f'./Craters/craters{craterID}.png'

                for item in planetColorsUsed:
                    if item['surface']:
                        if item['surface']['file'] == surfaceFile and item['planet'] == planetColor:
                            # print(f"File '{item['surface']['file']}' is the same as '{surfaceFile}' and Color '{item['planet']} is the same as '{planetColor}'")
                            duplicatedSurfacePlanet = True
                            break

                if duplicatedCrater == False:
                    break

           
            planetColorsUsed.append({
                'planet': planetColor,
                'surface': {
                    'file': craterFile,
                    'color': ''
                }
            })

            if craterFile:
                planet = generatePlanet(planetColor, planetFile)
                insertCrater(planet, craterFile)
                surfaceFile = craterFile
                # print(f'{i}: Crater')


        else:

            duplicatedPlanet = False

            for j, item in enumerate(planetColorsUsed):
                if item['planet'] == planetColor and item['surface'] == '':
                    # print(f"({i}) {planetColor} is the same as ({j + 1}) {item['planet']}")
                    duplicatedPlanet = True
                    break

            while duplicatedPlanet == True:
                # print('in here')

                duplicatedPlanet = False
                # planetNumber = random.randint(0,134)
                planetNumber = random.randint(0,134)
                planetColor = colorsList[planetNumber][0]

                for item in planetColorsUsed:
                    if item['planet'] == planetColor:
                        # print(f"SECOND LOOP: {planetColor} is the same as {item['planet']}")
                        duplicatedPlanet = True
                        break

                if duplicatedPlanet == False:
                    break

            planetColorsUsed.append({
                'planet': planetColor,
                'surface': ''
            })

            planet = generatePlanet(planetColor, planetFile)

            surfaceFile = 'Gas'


        # while planetColor in planetColorsUsed:
        #     pr = random.randint(0,255)
        #     pg = random.randint(0,255)
        #     pb = random.randint(0,255)

        #     planetColor = (pr,pg,pb)
    

    addShadow(planet)

    ringState = random.randint(1,5)

    hasRing = "No"

    if ringState % 3 == 0:

        ringColorsGroup = random.randint(0,len(ringColors) - 1)

        firstColor = ringColors[ringColorsGroup][0]
        secondColor = ringColors[ringColorsGroup][1]

        colors = [firstColor, secondColor]

        ring = insertRing(planet, ringColors[0])
        # ring = insertRing(planet, colors)

        hasRing = "Yes"


    jsonFile = f'./Metadata/{i}.json'
    # jsonFile = f'./MetadataTest/planet{i}.json'

    galaxy = random.randint(1,7)
    galaxy = random.randint(1,6)
    size = random.randint(3000,10000000)
    formatedSize = "{:,}".format(size)

    planetMetadata["name"] = f"Planet #{i}"
    planetMetadata["attributes"][0]["value"] = f"{galaxyNames[galaxy]}"
    planetMetadata["attributes"][1]["value"] = colorsList[planetNumber][1]
    planetMetadata["attributes"][3]["value"] = f"{formatedSize} km"
    planetMetadata["attributes"][4]["value"] = f"{hasRing}"

    if surfaceFile:
        if 'Lands' in surfaceFile:
            planetMetadata["attributes"][2]["value"] = "Land"
        elif 'Lines' in surfaceFile:
            planetMetadata["attributes"][2]["value"] = "Stripes"
        elif 'Craters' in surfaceFile:
            if '6' in surfaceFile:
                planetMetadata["attributes"][2]["value"] = "Rocks"
            else:
                planetMetadata["attributes"][2]["value"] = "Craters"
        elif 'Gas' in surfaceFile:
            planetMetadata["attributes"][2]["value"] = "Gas"

    # create background files with the name of the galaxy in it
    # if planetMetadata["atributes"][0]["value"] in background file: 

    insertBackground(planet, galaxies[galaxy], ring)

    improveResolution(planetFile)

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
#     # if not item['surface']:
#     print(f'{i}: {item}')

# print(planetColorsUsed[0]['surface']['color'])

# for i, item in enumerate(planetColorsUsed):
#     print(f'{i + 1}: {item}')