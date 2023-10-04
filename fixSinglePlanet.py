import numpy as np
from PIL import Image

def improveResolution(file):
    # file = './Planets/earth.png'
    im = Image.open(file).convert('RGB')
    im = im.resize((3000,3000),resample=Image.NEAREST)
    # im.save(f"./ImprovedPlanets/improvedPlanet2.png")
    im.save(file)