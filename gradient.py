from PIL import Image

def make_gradient(width, length):
    # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
    img = Image.new( 'RGB', (width, length), "black")
    pixels = img.load() # create the pixel map

    for i in range(img.size[0]):    # for every col:
        for j in range(img.size[1]):    # For every row
            pixels[i,j] = (int(i*255/width), 0, 0) # set the colour accordingly

    img.save("gradient.png", "PNG")


if __name__ == "__main__":
    make_gradient(500, 500);
