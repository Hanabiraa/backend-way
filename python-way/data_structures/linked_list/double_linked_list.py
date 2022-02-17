from platform import node
from turtle import circle
from typing import Any


class WrongPosition(Exception):
    pass


class _Node():
    """
    Node builder for DoubleLinkedList implementation
    """

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList():
    """
    My implementation of double linked list structure

    Ex:
    >>> l = DoubleLinkedList()
    >>> for data in range(5):
    >>>     l.insert_left(data)
    >>> print(l)
    [4] <-> [3] <-> [2] <-> [1] <-> [0]
    """

    def __init__(self) -> None:
        self.head = None

    def reverse(self) -> None:
        curr = self.head
        tmp = None
        while curr:
            tmp = curr.prev
            curr.prev = curr.next
            curr.next = tmp
            curr = curr.prev

        if tmp:
            self.head = tmp.prev

    def insert_left(self, data: Any) -> None:
        new_node = _Node(data)
        new_node.next = self.head
        new_node.prev = None
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_right(self, data: Any) -> None:
        new_node = _Node(data)
        if not self.head:
            self.head = new_node
            return

        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        new_node.next = tmp.next
        new_node.prev = tmp
        tmp.next = new_node

    def insert_after(self, pos: int, data: Any) -> None:
        if not pos:
            self.insert_left(data)
            return

        tmp = self.head
        for _ in range(pos):
            tmp = tmp.next
            if not tmp:
                raise WrongPosition(
                    "the specified position is outside the list")

        new_node = _Node(data)
        if tmp.next:
            tmp.next.prev = new_node
        new_node.next = tmp.next
        new_node.prev = tmp
        tmp.next = new_node

    def __str__(self) -> str:
        tmp = self.head
        template = "[{}] <-> "
        res = ""
        while tmp:
            res += template.format(tmp.data)
            tmp = tmp.next
        return res[:-5]


if __name__ == "__main__":
    l = DoubleLinkedList()

    for data in range(5):
        l.insert_left(data)
    for data in range(-1, -5, -1):
        l.insert_right(data)

    l.insert_after(0, 500)
    l.insert_after(1, 250)
    l.insert_after(10, -500)
    l.insert_after(10, -1000)
    print(l)
    l.reverse()
    print(l)
