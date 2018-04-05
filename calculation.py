from PIL import Image
import numpy as np
import os
import random

def fill_hole(filepath, HALF_HOLE_WIDTH, HALF_HOLE_LENGTH):
    modified = Image.open(filepath)

    width = modified.size[0] # default = 1000
    length = modified.size[1] # default = 500
    middle_width = int(width / 2)
    middle_length = int(length / 2)

    # for now, hole detection range in image is not needed

    pixel_array = np.array(modified)
    edit_left = np.copy(pixel_array)
    edit_right = np.copy(pixel_array)
    edit_left, edit_right = edit_left.astype(float), edit_right.astype(float)

    random_element_copy(edit_left, edit_right, middle_width, middle_length, HALF_HOLE_WIDTH, HALF_HOLE_LENGTH, width, length)
    average_bounds(edit_left, 20, middle_width, middle_length, HALF_HOLE_WIDTH, HALF_HOLE_LENGTH)
    float_array_to_pixel_array(edit_left, pixel_array, middle_width, middle_length, HALF_HOLE_WIDTH, HALF_HOLE_LENGTH)


    calculated = Image.fromarray(pixel_array)
    filename, file_extension = os.path.splitext(filepath)

    calculated.save('calculated img/' + os.path.basename(filename) + '_removed_one_side.png', "PNG")

def gradient_by_row(edit_left, edit_right, middle_width, middle_length, HALF_HOLE_WIDTH, HALF_HOLE_LENGTH, width, length):
    for j in range(middle_length - HALF_HOLE_LENGTH, middle_length + HALF_HOLE_LENGTH):
        for i in range(middle_width - HALF_HOLE_WIDTH, middle_width + HALF_HOLE_WIDTH):
            total_change_from_left = 0
            reach = 20
            for counter in range(i - reach, i):
                total_change_from_left = total_change_from_left + (edit_left[j][i-1] - edit_left[j][i-1-counter]) / counter
            edit_left[j][i] = edit_left[j][i-1] + (total_change_from_left / reach)

            total_change_from_right = 0
            for counter in range(i, i + reach):
                total_change_from_right = total_change_from_right + (edit_right[j][i+1] - edit_right[j][i+1+counter]) / counter
            edit_right[j][width - i] = edit_right[j][width - i + 1] + (total_change_from_right / reach)

def random_element_copy(edit_left, edit_right, middle_width, middle_length, HALF_HOLE_WIDTH, HALF_HOLE_LENGTH, width, length):
    for j in range(middle_length - HALF_HOLE_LENGTH, middle_length + HALF_HOLE_LENGTH):
        for i in range(middle_width - HALF_HOLE_WIDTH, middle_width + HALF_HOLE_WIDTH):
            edit_left[j][i] = edit_left[j][i-random.randint(1, 300)]
            edit_right[j][width - i] = edit_right[j][width - i + random.randint(1, 300)]

def average_bounds(edit_array, bounds, middle_width, middle_length, HALF_HOLE_WIDTH, HALF_HOLE_LENGTH):
    for j in range(middle_length - HALF_HOLE_LENGTH, middle_length + HALF_HOLE_LENGTH):
        for i in range(middle_width - HALF_HOLE_WIDTH, middle_width + HALF_HOLE_WIDTH):
            if (j < (middle_length - HALF_HOLE_LENGTH + bounds)):
                edit_array[j][i] = np.sqrt((edit_array[j+1][i]*edit_array[j+1][i] +
                                        edit_array[j+1][i+1]*edit_array[j+1][i+1]  +
                                        edit_array[j+1][i-1]*edit_array[j+1][i-1]) / 3)
            elif (j > (middle_length + HALF_HOLE_LENGTH - bounds)):
                edit_array[j][i] = np.sqrt((edit_array[j-1][i]*edit_array[j-1][i] +
                                        edit_array[j-1][i+1]*edit_array[j-1][i+1]  +
                                        edit_array[j-1][i-1]*edit_array[j-1][i-1]) / 3)

            elif (i < (middle_width - HALF_HOLE_WIDTH + bounds)):
                edit_array[j][i] = np.sqrt((edit_array[j][i-1]*edit_array[j][i-1] +
                                        edit_array[j+1][i-1]*edit_array[j+1][i-1] +
                                        edit_array[j-1][i-1]*edit_array[j-1][i-1]
                                        ) / 3)
            elif (i > (middle_width + HALF_HOLE_WIDTH - bounds)):
                edit_array[j][i] = np.sqrt((edit_array[j][i+1]*edit_array[j][i+1] +
                                        edit_array[j+1][i+1]*edit_array[j+1][i+1] +
                                        edit_array[j-1][i+1]*edit_array[j-1][i+1]
                                        ) / 3)

def average_with_surrounding(edit_array, middle_width, middle_length, HALF_HOLE_WIDTH, HALF_HOLE_LENGTH):
    for j in range(middle_length - HALF_HOLE_LENGTH, middle_length + HALF_HOLE_LENGTH):
        for i in range(middle_width - HALF_HOLE_WIDTH, middle_width + HALF_HOLE_WIDTH):
            edit_array[j][i] = np.sqrt((edit_array[j][i+1]*edit_array[j][i+1] + edit_array[j][i-1]*edit_array[j][i-1] +
                                    edit_array[j+1][i]*edit_array[j+1][i] + edit_array[j-1][i]*edit_array[j-1][i] +
                                    edit_array[j+1][i+1]*edit_array[j+1][i+1] + edit_array[j-1][i+1]*edit_array[j-1][i+1] +
                                    edit_array[j-1][i-1]*edit_array[j-1][i-1] + edit_array[j+1][i-1]*edit_array[j+1][i-1]) / 8)

def float_array_to_pixel_array(edit_array, pixel_array, middle_width, middle_length, HALF_HOLE_WIDTH, HALF_HOLE_LENGTH):
    for j in range(middle_length - HALF_HOLE_LENGTH, middle_length + HALF_HOLE_LENGTH):
        for i in range(middle_width - HALF_HOLE_WIDTH, middle_width + HALF_HOLE_WIDTH):
            pixel_array[j][i] = edit_array[j][i].astype(int)

def weighted_average_array(edit_left, edit_right, pixel_array, middle_width, middle_length, HALF_HOLE_WIDTH, HALF_HOLE_LENGTH):
    for j in range(middle_length - HALF_HOLE_LENGTH, middle_length + HALF_HOLE_LENGTH):
        for i in range(middle_width - HALF_HOLE_WIDTH, middle_width + HALF_HOLE_WIDTH):
            weight_left = middle_width + HALF_HOLE_WIDTH - i
            weight_right = i - (middle_width - HALF_HOLE_WIDTH)

            pixel_array[j][i] = np.sqrt(((weight_left)*edit_left[j][i]*edit_left[j][i] + (weight_right)*edit_right[j][i]*edit_right[j][i]) / (2*HALF_HOLE_WIDTH))

if __name__ == "__main__":
    fill_hole("intermediate img/image_01_hole.png", 200, 200)
