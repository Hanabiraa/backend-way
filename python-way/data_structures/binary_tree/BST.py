"""
This module implement BST (Binary search tree) and their basic operations:
1. insert
2. delete
3. find
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
    """

    def __init__(self) -> None:
        self.root = None

    def add(self, data: Any) -> None:
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
