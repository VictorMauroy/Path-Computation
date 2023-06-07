import random
from random import randint
from path_calculation import calculate_distance
from tree import Tree

# dict of str : tuple
planet_positions = {
    "origin" : (0, 0)
}
random.seed(67)

planet_positions["a_point"] = (randint(-500, 500), randint(-500, 500))
planet_positions["b_point"] = (randint(-500, 500), randint(-500, 500))
planet_positions["c_point"] = (randint(-500, 500), randint(-500, 500))

root_tree = Tree('origin', planet_positions['origin'], )
root_tree.create_tree_from_dictionary(planet_positions) # generate tree from dictionary

# print(root_tree.browse_depth()) # Obtenir la liste en profondeur des éléments de l'arbre.
list_of_leaves:list[Tree] = root_tree.get_all_leafs()
for leaf in list_of_leaves :
    print(leaf.name, end = " ")

# print(f"A point is equal to : {planet_positions['a_point']}")
# print(f"B point is equal to : {planet_positions['b_point']}")
# print(f"{calculate_distance(planet_positions['a_point'],planet_positions['b_point'])}")