from PIL import Image
import numpy as np

def fill_hole(HALF_HOLE_WIDTH, HALF_HOLE_LENGTH):
    modified = Image.open("gradientWithHole.png")
    # pixels = modified.load()
    # print(type(pixels))
    width = modified.size[0] # default = 1000
    length = modified.size[1] # default = 500

    # for now, hole detection range in image is not needed

    pixel_array = np.array(modified)
    edit = np.copy(pixel_array)

    edit = edit.astype(float)
    for j in range(int(length / 2) - HALF_HOLE_LENGTH, int(length / 2) + HALF_HOLE_LENGTH):
        for i in range(int(width / 2) - HALF_HOLE_WIDTH, int(width /2) + HALF_HOLE_WIDTH):
            # changes only by row
            sum = 0
            reach = 10
            for counter in range(i - reach, i):
                sum = sum + (edit[j][i-1] - edit[j][i-1-counter]) / counter

            #expectedDiff = sum / (reach)
            #print(expectedDiff)
            edit[j][i] = edit[j][i-1] + (sum /reach)

            pixel_array[j][i] = edit[j][i].astype(int)

    # for i in range(int(width / 2) - HALF_HOLE_WIDTH, int(width /2) + HALF_HOLE_WIDTH):
    #     print(pixel_array[int(length / 2) - 1][i])

    # for j in range(int(length / 2) - 100, int(length / 2) + 100):
    #     for i in range(int(width / 2) - 100, int(width /2) + 100):
    #         prevDiff = tuple(x - y for x, y in zip(modified.getpixel((i-1, j)), modified.getpixel((i-2, j))))
    #         #prevDiff = tuple(map(lambda x, y: x - y, modified.getpixel((i-1, j)), modified.getpixel((i-2, j))))
    #         pixels[i, j] = tuple(x + y for x, y in zip(modified.getpixel((i-1, j)), prevDiff))

    calculated = Image.fromarray(pixel_array)
    calculated.save("calculated.png", "PNG")
