##### How to proceed ? #####
# We will receive a tree of data : the points are generated on different paths which excludes
# the points already added.
# We must check each branch, calculate the distance between each points and save the values.

# At the end, we will return the list/dictionary of values with the smallest sum of distances.

from tree import Tree
import math

def calculate_distance(first_point:tuple, second_point:tuple) -> float :
    """Take two points (vector 2) and return the distance between them (float)"""
    x1, y1 = first_point
    x2, y2 = second_point
    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2
    )

#def find_shortest_path(tree_of_paths:Tree) -> tuple(list, float) :
    """_summary_

    Returns:
        tuple (list, int): First, return a list of point, ordered to have the smallest sum of distances.
        second, return the sum of the distances finded.
    """

#def calculate_path_sum(leaf:Tree) -> float:
    """Calculate the distance from a leaf and each parents and return the sum of distances
    That function will call multiple time the function 'calculate_distance'"""

# Reçoit une liste comprenant chaque chemin possible (successions de points) et la somme de leurs distances.
#def compare_distance_of_lists(path_finded:list(tuple(list, float))) -> tuple(list, float) :
    """"""