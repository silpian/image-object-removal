from PIL import Image

def make_hole(filepath, HALF_HOLE_WIDTH, HALF_HOLE_LENGTH):
    original = Image.open(filepath)
    pixels = original.load()

    width = original.size[0] # default = 1000
    length = original.size[1] # default = 500

    # "delete" some pixels - change to BLACK as default
    for i in range(int(width / 2) - HALF_HOLE_WIDTH, int(width / 2) + HALF_HOLE_WIDTH):
        for j in range(int(length / 2) - HALF_HOLE_LENGTH, int(length / 2) + HALF_HOLE_LENGTH):
            pixels[i, j] = (0, 0, 0)

    # since pixels is a reference map to original, the image has been changed
    original.save("gradientWithHole.png", "PNG")

if __name__ == "__main__":
    make_hole("gradient.png", 50, 50)
