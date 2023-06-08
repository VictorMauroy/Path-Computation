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

def find_shortest_path(root:Tree) :
    """Check each path of a tree and return the one with the lowest distance to visit each point. 

    Returns:
        tuple (list, int): First, return a list of trees, from the leaf/bottom of the tree to the origin.
        second, return the sum of the distances between each points of the smallest path of the tree.
    """
    myleaves:list[Tree] = root.get_all_leafs()
    list_distances = []

    for leaf in myleaves :
        list_distances.append(calculate_path_sum(leaf))
    
    index_where_is_min = 0
    minimal_distance_founded:int = 99999999999999999999999999999999999999999999

    for i in range(len(list_distances)) :
        if list_distances[i] < minimal_distance_founded :
            minimal_distance_founded = list_distances[i]
            index_where_is_min = i

    best_path = [myleaves[index_where_is_min]]
    waiting_queue = best_path.copy()
    while len(waiting_queue)>0 :
        if not waiting_queue[0].is_root() :
            best_path.append(waiting_queue[0].parent_branch)
            waiting_queue.append(waiting_queue[0].parent_branch)
        waiting_queue.pop(0)
    
    return best_path, minimal_distance_founded

def calculate_path_sum(leaf:Tree) -> float:
    """Calculate the distance from a leaf and each parents and return the sum of distances
    That function will call multiple time the function 'calculate_distance'"""
    waiting_queue:list[Tree] = []
    distance = 0
    if leaf.is_root() :
        return 0
    
    waiting_queue.append(leaf)
    while len(waiting_queue) > 0 :
        if not waiting_queue[0].is_root() :
            distance += calculate_distance(waiting_queue[0].coordonates, waiting_queue[0].parent_branch.coordonates)
            waiting_queue.append(waiting_queue[0].parent_branch)
        waiting_queue.pop(0)
    
    return distance