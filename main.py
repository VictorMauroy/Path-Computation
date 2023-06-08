import random
from random import randint
from path_calculation import find_shortest_path
from tree import Tree

# dict of str with tuple values (coordonates)
planet_positions = {
    "origin" : (0, 0)
}
random.seed(67)

planet_positions["a_point"] = (randint(-500, 500), randint(-500, 500))
planet_positions["b_point"] = (randint(-500, 500), randint(-500, 500))
planet_positions["c_point"] = (randint(-500, 500), randint(-500, 500))

root_tree = Tree('origin', planet_positions['origin'], )
root_tree.create_tree_from_dictionary(planet_positions) # generate tree from dictionary

#region Optimized path calculation 
optimised_path:list[Tree]
optimised_path, minDistance = find_shortest_path(root_tree)

tree_names:str = []
for tree in optimised_path :
    tree_names.append(tree.name)

print(f"The most optimized path is : {tree_names[::-1]} with a distance of : {minDistance}")
#endregion
