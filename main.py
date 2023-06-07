import random
from random import randint
from path_calculation import calculate_distance

# dict of str : tuple
planet_positions = {
    "origin" : (0, 0)
}
random.seed(67)

planet_positions["a_point"] = (randint(-500, 500), randint(-500, 500))
planet_positions["b_point"] = (randint(-500, 500), randint(-500, 500))
planet_positions["c_point"] = (randint(-500, 500), randint(-500, 500))

print(f"A point is equal to : {planet_positions['a_point']}")
print(f"B point is equal to : {planet_positions['b_point']}")

print(f"{calculate_distance(planet_positions['a_point'],planet_positions['b_point'])}")