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


if __name__ == "__main__":
    main()
