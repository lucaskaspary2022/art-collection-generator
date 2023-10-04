from test import generatePlanet
from insertLines import addSurface
from shadow import addShadow
from nftColors import colorsList
from addCrater import insertCrater
from addRing import insertRing
from addBackground import insertBackground
from addRing import insertRing
from fixSinglePlanet import improveResolution


generatePlanet((107,89,138), './PlanetTests/planetTest4.png')

insertCrater('./PlanetTests/planetTest4.png', './Craters/newCrater.png')

# insertCrater('./PlanetTests/planetTest1.png', './Rock/rock1.png')
# addSurface('./PlanetTests/planetTest2.png', './Lines/lines4.png', (29,191,115))

addShadow('./PlanetTests/planetTest4.png')

insertRing('./PlanetTests/planetTest4.png', [(181,181,181),(230,230,230)])

insertBackground('earth.png', './Backgrounds/background7.png', False)

improveResolution('earth.png')