from PIL import Image

planet = Image.open('test.png')
border = Image.open('border.png')

planet.paste(border, (0,0), border)

resized_img = planet.resize((300, 300), resample=Image.NEAREST)
resized_img.save('generatedPlanet.png')