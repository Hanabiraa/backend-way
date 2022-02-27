"""
this module shows simple binary tree, 3 other traversals and 
functions for checking whether a binary tree is complete, perfect, full and balanced
"""

from typing import Any


class Node:
    def __init__(self, val: Any, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)


def traversal_inorder(root: Node) -> str:
    """
    Stack realization.

    1. Visit all the nodes in the left subtree
    2. Print root node
    3. Visit all the nodes in the right subtree
    """
    stack = []
    res = ""
    template = "{} -> "
    while True:
        if root:
            stack.append(root)
            root = root.left
        elif stack:
            root = stack.pop()
            res += template.format(str(root))
            root = root.right
        else:
            break
    return res[:-4]


def traversal_preorder(root: Node) -> str:
    """
    Stack realization.

    1. Print root node
    2. Visit all the nodes in the left subtree
    3. Visit all the nodes in the right subtree
    """
    stack = []
    res = ""
    template = "{} -> "
    while True:
        if root:
            res += template.format(str(root))
            stack.append(root)
            root = root.left
        elif stack:
            root = stack.pop().right
        else:
            break
    return res[:-4]


def traversal_postorder(root: Node) -> str:
    """
    Two-Stack realization.

    1. Visit all the nodes in the left subtree
    2. Visit all the nodes in the right subtree
    3. Print root node
    """
    stack1 = []
    stack2 = []
    res = ""
    template = "{} -> "

    stack1.append(root)
    while stack1:
        root = stack1.pop()
        stack2.append(root)

        if root.left:
            stack1.append(root.left)
        if root.right:
            stack1.append(root.right)

    while stack2:
        root = stack2.pop()
        res += template.format(root)
    return res[:-4]


def bin_tree_is_full(root: Node) -> bool:
    """
    checks if the tree is full 

    A full Binary tree is a special type of binary tree in which every parent
    node/internal node has either two or no children.
    """
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return bin_tree_is_full(root.left) and bin_tree_is_full(root.right)

    return False


def bin_tree_is_perfect(root: Node) -> bool:
    """
    checks if the tree is perfect

    A perfect binary tree is a type of binary tree in which every internal node
    has exactly two child nodes and all the leaf nodes are at the same level.
    """
    max_depth = curr_depth = 0
    tmp_root = root
    while tmp_root.left:
        max_depth += 1
        tmp_root = tmp_root.left

    def check(root, max_depth: int, curr_depth: int) -> bool:
        if root is None:
            return True

        if root.left is None and root.right is None:
            return max_depth == curr_depth

        if root.left is None or root.right is None:
            return False

        return check(root.left, max_depth, curr_depth+1) and check(root.right, max_depth, curr_depth+1)

    return check(root, max_depth, curr_depth)


def bin_tree_is_complete(root: Node) -> bool:
    """
    checks if the tree is complete

    Use index property.
    If the index of any element in the array is `i`, the element in the index `2i+1` will become
    the left child and element in `2i+2` index will become the right child.
    Also, the parent of any element at index `i` is given by the lower bound of `(i-1)/2`.
    """
    def count_nodes(root: Node) -> int:
        """
        count all nodes in tree
        """
        if root is None:
            return 0
        return 1 + count_nodes(root.left) + count_nodes(root.right)

    def check(root: Node, index: int, max_node: int) -> bool:
        if root is None:
            return True
        if index >= max_node:
            return False
        return check(root.left, 2*index+1, max_node) and check(root.right, 2*index+2, max_node)
    return check(root, 0, count_nodes(root))


def bin_tree_is_balanced(root: Node) -> bool:
    """
    checks if the tree is balance

    An empty tree is height-balanced. A non-empty binary tree T is balanced if: 
    1) Left subtree of T is balanced 
    2) Right subtree of T is balanced 
    3) The difference between heights of left subtree and right subtree is not more than 1. 
    """
    def height(root: Node) -> int:
        """
        count height for curr sub-tree
        """
        if root is None:
            return 0
        return 1 + max(height(root.left), height(root.right))

    def check(root: Node) -> bool:
        if root is None:
            return True

        l_height = height(root.left)
        r_height = height(root.right)
        if 0 <= abs(l_height - r_height) <= 1 and check(root.left) and check(root.right):
            return True
        return False
    return check(root)

def main():
    """ 
    Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   
    """
    tree1 = Node(1, Node(2,  Node(4), Node(5)), Node(3))
    print("inorder:\t", traversal_inorder(tree1))
    print("preorder:\t", traversal_preorder(tree1))
    print("postorder:\t", traversal_postorder(tree1))
    print("Is this tree full?: ", bin_tree_is_full(tree1))

    """ 
    Constructed binary tree is
            1
          /   \
         2     3
       / 
      4      
    """
    tree2 = Node(1, Node(2,  Node(4)), Node(3))
    print("Is this tree full?: ", bin_tree_is_full(tree2))

    """ 
    Constructed binary tree is
            1
          /   \
         2     3
        / \   / \
       4   5 8   9
    """
    tree3 = Node(1, Node(2,  Node(4), Node(5)), Node(3, Node(8), Node(9)))
    print("Is this tree perfect?: ", bin_tree_is_perfect(tree3))
    print("Is this tree perfect?: ", bin_tree_is_perfect(tree2))

    """ 
    Constructed binary tree is
            1
          /   \
         2     3
              / \
             8   9
    """
    tree4 = Node(1, Node(2), Node(3, Node(8), Node(9)))
    print("Is this tree complete?: ", bin_tree_is_complete(tree1))
    print("Is this tree complete?: ", bin_tree_is_complete(tree4))

    """ 
    Constructed binary tree is
            1
          /   \
         2     3
              / \
             8   9
            /
           3
    """
    tree5 = Node(1, Node(2), Node(3, Node(8, Node(3)), Node(9)))
    print("Is this tree height-balanced?: ", bin_tree_is_balanced(tree1))
    print("Is this tree height-balanced?: ", bin_tree_is_balanced(tree5))
if __name__ == "__main__":
    main()
