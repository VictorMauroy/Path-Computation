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
    """_summary_

    Returns:
        tuple (list, int): First, return a list of point, ordered to have the smallest sum of distances.
        second, return the sum of the distances finded.
    """
    myleaves:list[Tree] = root.get_all_leafs()
    list_distances=[]

    for leaf in myleaves :
        list_distances.append(calculate_path_sum(leaf))
    
    index_where_is_min = 0
    minDistanceFounded:int = 99999999999999999999999999999999999999999999

    for i in range(len(list_distances)) :
        if list_distances[i] < minDistanceFounded :
            minDistanceFounded = list_distances[i]
            index_where_is_min = i

    best_path = [myleaves[index_where_is_min]]
    file_attente = [myleaves[index_where_is_min]]
    while len(file_attente)>0 :
        if not file_attente[0].is_root() :
            best_path.append(file_attente[0].parent_branch)
            file_attente.append(file_attente[0].parent_branch)
        file_attente.pop(0)
    
    return best_path, minDistanceFounded

def calculate_path_sum(leaf:Tree) -> float:
    """Calculate the distance from a leaf and each parents and return the sum of distances
    That function will call multiple time the function 'calculate_distance'"""
    queue:list[Tree] = []
    distance = 0
    if leaf.parent_branch == None :
        return 0
    
    queue.append(leaf)
    while len(queue)>0 :
        if not queue[0].is_root() :
            distance += calculate_distance(queue[0].coordonates, queue[0].parent_branch.coordonates)
            queue.append(queue[0].parent_branch)
        queue.pop(0)
    
    return distance