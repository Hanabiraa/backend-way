"""
This module implement BST (Binary search tree) and their basic operations:
1. insert
2. delete
"""
from typing import Any, Union, Optional


class _Node:
    """
    Class builder for binary tree
    """

    def __init__(self, data: Any) -> None:
        self.data = data
        self.left = None
        self.right = None


class BST:
    """
    My BST implemention

    Example:
    >>> tree = BST()
    >>> for data in [30, 50, 15, 20, 10, 40, 60]:
    >>>     tree.add(data)
    >>> print(tree)
    [10, 15, 20, 30, 40, 50, 60]
    """

    def __init__(self) -> None:
        self.root = None

    def add(self, data: Any) -> None:
        """
        add node non-recursive way
        """
        new_node = _Node(data)
        if not self.root:
            self.root = new_node
            return

        prev = None
        curr = self.root
        while curr:
            if new_node.data < curr.data:
                prev = curr
                curr = curr.left
            elif new_node.data > curr.data:
                prev = curr
                curr = curr.right
        else:
            if new_node.data < prev.data:
                prev.left = new_node
            elif new_node.data > prev.data:
                prev.right = new_node

    def delete(self, data: Any) -> None:
        """
        delete node recursive way
        """
        self.__delete(self.root, data)

    @staticmethod
    def __delete(root, data):
        if not root:
            return root
        
        if data < root.data:
            root.left = BST.__delete(root.left, data)
        elif data > root.data:
            root.right = BST.__delete(root.right, data)
        else:
            if not root.left:
                tmp = root.right
                root = None
                return tmp
            elif root.right is None:
                tmp = root.left
                root = None
                return tmp
            tmp = BST.__min_value_node(root.right)
            root.data = tmp.data
            root.right = BST.__delete(root.right, tmp.data)
        return root

    @staticmethod
    def __min_value_node(root: _Node) -> Any:
        """
        find and return min val node
        """
        if root.left:
            return BST.__min_value_node(root.left)
        else:
            return root

    def __str__(self) -> str:
        """
        inorder traversal
        """
        res = []
        stack = []
        tmp = self.root
        while True:
            if tmp:
                stack.append(tmp)
                tmp = tmp.left
            elif stack:
                tmp = stack.pop()
                res.append(tmp.data)
                tmp = tmp.right
            else:
                break
        return str(res)


if __name__ == "__main__":
    tree = BST()
    for data in [30, 50, 15, 20, 10, 40, 60]:
        tree.add(data)
    print(tree)

    """ Let us create following BST
                50
              /     \
            30      70
           /  \    /  \
         20   40  60   80 
             /  \
            35  45
    """
    tree1 = BST()
    for data in [50, 30, 20, 40, 70, 60, 80, 45, 35]:
        tree1.add(data)
    print("before delete:\t\t", tree1)
    tree1.delete(20)
    print("after delete 20:\t", tree1)
    tree1.delete(30)
    print("after delete 30:\t", tree1)
    tree1.delete(50)
    print("after delete 50:\t", tree1)
