from gradient import make_gradient
from hole import make_hole
from calculation import fill_hole

from PIL import Image
import numpy as np

WIDTH = 700
LENGTH = 500

HALF_HOLE_WIDTH = 100
HALF_HOLE_LENGTH = 100

make_gradient(WIDTH, LENGTH)
make_hole("gradient.png", HALF_HOLE_WIDTH, HALF_HOLE_LENGTH)
fill_hole(HALF_HOLE_WIDTH, HALF_HOLE_LENGTH)
