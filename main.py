import random
from random import randint

# dict of str : tuple
planet_positions = {
    "origin" : (0, 0)
}
random.seed(67)

planet_positions["a_point"] = (randint(-500, 500), randint(-500, 500))
planet_positions["b_point"] = (randint(-500, 500), randint(-500, 500))
planet_positions["c_point"] = (randint(-500, 500), randint(-500, 500))

