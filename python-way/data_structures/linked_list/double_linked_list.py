from typing import Any


class WrongPosition(Exception):
    pass


class _Node:
    """
    Node builder for DoubleLinkedList implementation
    """

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
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
                raise WrongPosition("the specified position is outside the list")

        new_node = _Node(data)
        if tmp.next:
            tmp.next.prev = new_node
        new_node.next = tmp.next
        new_node.prev = tmp
        tmp.next = new_node

    def remove_left(self) -> Any:
        if not self.head:
            return None

        del_node = self.head
        if not self.head.next:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
        del_node.next = None
        del_node.prev = None
        return del_node.data

    def remove_right(self) -> Any:
        if not self.head or not self.head.next:
            return self.remove_left

        del_node = self.head

        while del_node.next:
            del_node = del_node.next
        del_node.prev.next = None
        del_node.prev = None
        del_node.next = None
        return del_node.data

    def remove_after(self, prev_node: _Node) -> Any:
        if not prev_node:
            return self.remove_left()

        if not prev_node.next:
            raise ValueError("No delete after")

        del_node = prev_node.next
        prev_node.next = del_node.next
        if after_node := del_node.next:
            after_node.prev = prev_node
        del_node.prev = None
        del_node.next = None
        return del_node.data

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

    for _ in range(5):
        print(f"del left: {l.remove_left()}")
    for _ in range(3):
        print(f"del right: {l.remove_right()}")
    print(l)
    l.reverse()
    print(l)
    del_ = l.head.next.next
    print(f"del after {del_.data}: ", l.remove_after(del_))
    print(f"del after {None}: ", l.remove_after(None))
    print(l)
    l.reverse()
    print(l)
