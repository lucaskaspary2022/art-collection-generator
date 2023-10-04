from PIL import Image

def removeBackground(image):

    # img = Image.open(file)
    # img = img.convert("RGBA")
    img = image.convert('RGBA')

    data = img.getdata()

    newData = []

    

    for item in data:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255,255,255,0))
        else:
            newData.append(item)

    img.putdata(newData)
    # .resize((300, 300), resample=Image.NEAREST)
    # img.save(file, 'PNG')

    return img