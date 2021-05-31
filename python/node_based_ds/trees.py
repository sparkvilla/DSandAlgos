import pdb

"""
A tree is a node-based data structure where each node can have links to
multiple nodes

example:

          j                first level
       /     \
      m       b            second level
     / \     /  \
    q   z    t   s         third level

some references:

    - 'j' is a parent to 'm' and 'b'
    - 'm' and 'b' are children of 'j'
    - a node can have descendents (all the nodes that stem from it) and ancestors
      (all the nodes that it stems from)
    - Tree has levels. Each level is a row in the tree
    - A tree is 'balanced' when its nodes subtrees have the same number of nodes
      in it

BINARY SEARCH TREE

- A binary tree is a tree in which each node has zero, one or two children.
- A binary search tree is a binary tree that also abides t the following:
    - A node's left descendents can only contain values that are less then the
      node itself. A node's right descendents can only contain values that are
      greater then the node itself

"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_child = left
        self.right_child = right

def search(search_val, node, steps=0):

    steps += 1
    if search_val == node.value:
        print(f'Found {node.value} in {steps} steps')
        return

    if search_val < node.value:
        search(search_val, node.left_child, steps)

    if search_val > node.value:
        search(search_val, node.right_child, steps)


def insert(value, node):
    if value < node.value:
        if node.left_child is None:
            node.left_child = TreeNode(value)
        else:
            insert(value, node.left_child)
    if value > node.value:
        if node.right_child is None:
            node.right_child = TreeNode(value)
        else:
            insert(value, node.right_child)

def traverse_tree(node):
    """
    Implement the 'inorder' tree traversal
    """
    if not node:
        return
    traverse_tree(node.left_child)
    print(node.value)
    traverse_tree(node.right_child)



if __name__ == '__main__':

    root = TreeNode(50)
    for el in [25, 10, 4, 11, 33, 30, 40, 75, 56, 52, 61, 89, 82, 95]:
        insert(el, root)


    traverse_tree(root)

    search(75, root)
