from PIL import Image

original = Image.open("gradient.png")
pixels = original.load()

width = original.size[0] # default = 1000
length = original.size[1] # default = 500

# "delete" some pixels - change to white as default
for i in range(int(width / 2) - 100, int(width / 2) + 100):
    for j in range(int(length / 2) - 100, int(length / 2) + 100):
        pixels[i, j] = (255, 255, 255)

# since pixels is a reference map to original, the image has been changed

original.save("gradientWithHole.png", "PNG")
