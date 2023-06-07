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

def calculate_distance(first_point:tuple, second_point:tuple) -> float :
    """Take two points (vector 2) and return the distance between them (float)"""

def find_shortest_path() -> list :
    """"""

