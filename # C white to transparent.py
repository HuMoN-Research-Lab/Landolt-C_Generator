# C white to transparent

# I repurposed code I found here:
# https://stackoverflow.com/questions/765736/how-to-use-pil-to-make-all-white-pixels-transparent

from PIL import Image

# white to transparent for circle

# grab the image
img = Image.open('imageFiles/circle.png')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("imageFiles/2_circle.png", "PNG")


##########################
# white to transparent for all C's

for x in range(98):

    img = Image.open(str('imageFiles/landoltC_'+str(x+1)+'.png'))
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(str('imageFiles/2_landoltC_'+str(x+1)+'.png'), "PNG")