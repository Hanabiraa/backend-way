"""
My AVL tree implementation
"""

from typing import Any, Callable, List, Generator, Iterator, Union


class _Node():
    """
    Node builder for AVL_Tree
    """

    def __init__(self, data: Any) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self) -> str:
        return str(self.data)


class AVL_Tree():
    """
    My AVL Tree implementation

    methods:
    insert(key)
    delete(key)
    inorder_traverse() -> str
    print_Tree()
    """

    def __init__(self) -> None:
        self.root = None

    def insert(self, data: Any) -> None:
        self.root = AVL_Tree.__insert_node(self.root, data)

    @staticmethod
    def __insert_node(root: _Node, data: Any) -> Union[_Node, Callable[[_Node, Any], _Node]]:
        """
        recursive insert new node as leaf in BST and then balance
        """
        if not root:
            return _Node(data)
        elif data < root.data:
            root.left = AVL_Tree.__insert_node(root.left, data)
        elif data > root.data:
            root.right = AVL_Tree.__insert_node(root.right, data)

        root.height = 1 + max(AVL_Tree.__get_height(root.left),
                              AVL_Tree.__get_height(root.right))
        return AVL_Tree.__balance(root, data)

    def delete(self, data: Any) -> None:
        self.root = AVL_Tree.__delete(self.root, data)

    def __delete(root: _Node, data: Any) -> Union[_Node, Callable[[_Node, Any], _Node]]:
        """
        recursive delete node and then balance
        """
        if not root:
            return root

        if data < root.data:
            root.left = AVL_Tree.__delete(root.left, data)
        elif data > root.data:
            root.right = AVL_Tree.__delete(root.right, data)
        else:
            if root.left is None:
                tmp = root.right
                root = None
                return tmp
            elif root.right is None:
                tmp = root.left
                root = None
                return tmp
            tmp = AVL_Tree.__get_min_val_node(root.right)
            root.data = tmp.data
            root.right = AVL_Tree.__delete(root.right, tmp.data)

        root.height = 1 + max(AVL_Tree.__get_height(root.left),
                              AVL_Tree.__get_height(root.right))
        return AVL_Tree.__balance(root, data)

    @staticmethod
    def __balance(root: _Node, data: Any) -> Union[_Node, Callable[[_Node], _Node]]:
        balance = AVL_Tree.__get_balance(root)
        if balance > 1 and data < root.left.data:
            return AVL_Tree.__rotate_right(root)

        if balance > 1 and data > root.left.data:
            root.left = AVL_Tree.__rotate_left(root.left)
            return AVL_Tree.__rotate_right(root)

        if balance < -1 and data > root.right.data:
            return AVL_Tree.__rotate_left(root)

        if balance < -1 and data < root.right.data:
            root.right = AVL_Tree.__rotate_right(root.right)
            return AVL_Tree.__rotate_left(root)
        return root

    @staticmethod
    def __rotate_left(root: _Node) -> _Node:
        rotate_node = root.right
        root.right = rotate_node.left
        rotate_node.left = root

        root.height = 1 + max(AVL_Tree.__get_height(root.left),
                              AVL_Tree.__get_height(root.right))
        rotate_node.height = 1 + max(AVL_Tree.__get_height(rotate_node.left),
                                     AVL_Tree.__get_height(rotate_node.right))
        return rotate_node

    def __rotate_right(root: _Node) -> _Node:
        rotate_node = root.left
        root.left = rotate_node.right
        rotate_node.right = root

        root.height = 1 + max(AVL_Tree.__get_height(root.left),
                              AVL_Tree.__get_height(root.right))
        rotate_node.height = 1 + max(AVL_Tree.__get_height(rotate_node.left),
                                     AVL_Tree.__get_height(rotate_node.right))
        return rotate_node

    @staticmethod
    def __get_height(root: _Node) -> int:
        if not root:
            return 0
        return root.height

    @staticmethod
    def __get_balance(root: _Node) -> Union[int, Callable[[_Node], int]]:
        if root:
            return AVL_Tree.__get_height(root.left) - AVL_Tree.__get_height(root.right)
        return 0

    @staticmethod
    def __get_min_val_node(root: _Node) -> Union[Callable[[_Node], _Node], _Node]:
        if root.left is not None:
            return AVL_Tree.__get_min_val_node(root.left)
        return root

    def print_Tree(self) -> None:
        self.__print_tree(self.root, "", True)

    @staticmethod
    def __print_tree(root: _Node, indent: str, is_right: bool) -> Union[None, Callable[[_Node, str, bool], None]]:
        if root:
            print(indent, end="")
            if is_right:
                print("R____", end="")
                indent += "     "
            else:
                print("L____", end="")
                indent += "|    "
            print(f"({root}, {root.height})")
            AVL_Tree.__print_tree(root.left, indent, False)
            AVL_Tree.__print_tree(root.right, indent, True)

    def inorder_traverse(self) -> str:
        tmp = self.root
        cache = []
        res = []
        while True:
            if tmp:
                cache.append(tmp)
                tmp = tmp.left
            elif cache:
                tmp = cache.pop()
                res.append(tmp.data)
                tmp = tmp.right
            else:
                break
        return str(res)

    def _inorder_traverse_use_yield(self) -> List[Generator]:
        """
        testing strange method to traverse

        !WARNING: do not use this method. Its a prototype.
        """
        def _traverse_use_yield(root: _Node) -> Iterator[_Node]:
            if root:
                yield from _traverse_use_yield(root.left)
                yield root.data
                yield from _traverse_use_yield(root.right)
        return list(_traverse_use_yield(self.root))


if __name__ == "__main__":
    t = AVL_Tree()
    n1 = [33, 13, 52, 9, 21, 61, 8, 11, 95, 104, 23]
    n2 = [10, 20, 30, 40, 50, 25]
    n3 = [9, 5, 10, 0, 6, 11, -1, 1, 2]

    for data in n2:
        t.insert(data)

    t.print_Tree()
    print("inorder: \t{}".format(t.inorder_traverse()))
    print("yield inorder: \t{}".format(t._inorder_traverse_use_yield()))

    t.delete(20)
    t.print_Tree()
    print("inorder: \t{}".format(t.inorder_traverse()))
    print("yield inorder: \t{}".format(t._inorder_traverse_use_yield()))
