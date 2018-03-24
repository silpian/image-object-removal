from PIL import Image

modified = Image.open("gradientWithHole.png")
pixels = modified.load()

width = modified.size[0] # default = 1000
length = modified.size[1] # default = 500

# for now, hole detection range in image is not needed

for i in range(int(width / 2) - 100, int(width / 2) + 100):
    for j in range(int(length / 2) - 100, int(length /2) + 100):
        prevDiff = tuple(map(lambda x, y: x - y, modified.getpixel((i-1, j)), modified.getpixel((i-2, j))))
        print(prevDiff)
        pixels[i, j] = tuple(map(lambda x, y: x - y, modified.getpixel((i-1, j)), prevDiff))


# since pixels is a reference map to modified, the image has been changed

modified.save("calculated.png", "png")
