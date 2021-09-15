from binary_tree import BinaryTree
import math
class HierachicalCluster(BinaryTree):
    def __init__(self, name, root=None, left_child=None, right_child=None, distance=0):
        self.name = name
        self.root = root
        self.left_child = left_child
        self.right_child = right_child
        self.distance = distance

    def __getitem__(self, index):
        return self.root[index]

    def __len__(self):
        return len(self.root)

    def compute_centroid(self):
        centroid = []
        if self.left_child is None and self.right_child is None:
            return self.root
        else:
            rc = self.right_child.get_leaf_count()
            lc = self.left_child.get_leaf_count()

            for i in range(len(self.right_child)):
                val = ((self.right_child[i]*rc + self.left_child[i]*lc) / (rc+lc))
                centroid.append(val)
        self.root = centroid
        return self.root

    def get_leaf_count(self):
        if self.left_child == None:
            return 1
        else:
            return self.left_child.get_leaf_count() + self.right_child.get_leaf_count()


    def set_right_child(self, r_child):
        self.right_child = r_child

    def set_left_child(self, l_child):
        self.left_child = l_child

    def is_leaf(self):
        return self.left_child == None and self.right_child == None

    def get_root(self):
        return self.root
    
    def get_distance(self):
        return self.distance

    def get_display_name(self):
        if self.is_leaf():
            return self.name
        else:
            return str(round(self.distance, 2))

    def print(self):
        thislevel = [self]
        while thislevel:
            nextlevel = []
            for n in thislevel:
                print(n.get_display_name()+' ', end='')
                if n.left_child:
                    nextlevel.append(n.left_child)
                if n.right_child:
                    nextlevel.append(n.right_child)
            print('')
            thislevel = nextlevel

    def get_all_leaves(self):
        leaves = []
        self.get_all_leaves_rc(self, leaves)
        return leaves

    def get_all_leaves_rc(self, hc, leaves):
        if hc is None:
            return
        hc.get_all_leaves_rc(hc.left_child, leaves)
        hc.get_all_leaves_rc(hc.right_child, leaves)
        if hc.left_child is None and hc.right_child is None:
            leaves.append(hc)