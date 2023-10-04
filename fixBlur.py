import numpy as np
from PIL import Image

planets = [806, 7150, 8430, 7538, 7550]

for planet in planets:
    file = f'./Planets/planet{planet}.png'
    im = Image.open(file).convert('RGB')
    im = im.resize((3000,3000),resample=Image.NEAREST)
    im.save(f"./ImprovedPlanets/improvedPlanet{planet}.png")