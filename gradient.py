from PIL import Image

# gradient
width = 1000
length = 500
# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
img = Image.new( 'RGB', (width, length), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every col:
    for j in range(img.size[1]):    # For every row
        pixels[i,j] = (int(i*255/width), 0, 0) # set the colour accordingly

img.save("gradient.png", "PNG")
