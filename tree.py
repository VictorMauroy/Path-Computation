class Tree :
#region Initialization, add child and check leaf
    def __init__(self, name:str, coordonate:tuple[int, int], parent = None) -> None:
        self.parent_branch:Tree = parent
        self.name = name
        self.coordonates = coordonate
        self.child_branchs:list[Tree] = []
        

    def add_child(self, name:str, value:tuple, parent) -> None :
        """Initialize and add a child to the current branch"""
        new_child = Tree(name, value, parent)
        self.child_branchs.append(new_child)

    def is_leaf(self) -> bool :
        """Whether the current tree has childs branchs or not"""
        return not self.child_branchs
    
    def is_root(self) -> bool :
        """Whether the current tree is the root or not"""
        return not self.parent_branch != None
#endregion

    def get_depth(self) -> int :
        """Return the count of childs in the current tree"""
        if self.is_leaf() :
            return 1
        
        depth_list = [childBranch.get_depth() for childBranch in self.child_branchs]
        return max(depth_list) + 1

    def browse_depth(self, list_of_branchs:list = []) -> list :
        """Return the childs with their coordonates by using the depth browse method"""
        #print(f"{self.coordonates} is {'a leaf' if self.is_leaf() else 'not a leaf'}")
        
        if not self.is_leaf() :
            for branch in self.child_branchs :
                branch.browse_depth(list_of_branchs)
        
        list_of_branchs.append(self.name)

        return list_of_branchs

    def get_all_leafs(self, list_of_leaves:list = []) -> list :
        """Check a given tree and return all its leaves (last child without childs)"""
        for branch in self.child_branchs :
            if not branch.is_leaf() :
                branch.get_all_leafs(list_of_leaves)
            else :
                list_of_leaves.append(branch)
        
        return list_of_leaves

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