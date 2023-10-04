import numpy as np
from PIL import Image

file = f'notionPlanet.png'
im = Image.open(file).convert('RGB')
im = im.resize((280,280),resample=Image.NEAREST)
im.save(f"improvedNotionPlanet.png")