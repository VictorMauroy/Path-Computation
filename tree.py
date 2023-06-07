class Tree :
#region Initialization, add child and check leaf
    def __init__(self, name:str, coordonate:tuple[int, int], parent = None) -> None:
        self.name = name
        self.coordonates = coordonate
        self.child_branchs:list[Tree] = []
        self.parent_branch = parent

    def add_child(self, name:str, value:tuple, parent) -> None :
        """Initialize and add a child to the current branch"""
        new_child = Tree(name, value, parent)
        self.child_branchs.append(new_child)

    def is_leaf(self) -> bool :
        """Whether the current tree has childs branchs or not"""
        return not self.child_branchs
    
    def is_root(self) -> bool :
        """Whether the current tree is the root or not"""
        return not self.parent != None
#endregion

    def get_depth(self) -> int :
        """Return the count of childs in the current tree"""
        if self.is_leaf() :
            return 1
        
        depth_list = [childBranch.get_depth() for childBranch in self.child_branchs]
        return max(depth_list) + 1

    def get_all_leafs(self, tree_of_paths) -> list :
        """Check a given tree and return all its leafs (last childs without childs)"""

    def create_tree_from_dictionary(self, positions_dict:dict) :
        """Create one child for each element of the dictionary different of us and remove ourself

        Args:
            positions_dict (dict): Dictionary with the remaining position to create as a child branch.
        """
        saved_pos_dict = positions_dict.copy()
        if self.name in saved_pos_dict : # Check if 'key'(self.name) exists in dictionary
            saved_pos_dict.pop(self.name)
        
        # Check if the dictionary is empty !
        if not saved_pos_dict :
            return

        count = 0
        for key, value in saved_pos_dict.items() :
            self.add_child(key, value, self)
            self.child_branchs[count].create_tree_from_dictionary(saved_pos_dict)
            count += 1