from typing import Any


class _Node():
    """
    Node builder for circular single linked list implementation
    """

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None


class CircularSingleLinkedList():
    def __init__(self) -> None:
        self.last = None

    def append(self, data: Any) -> None:
        new_node = _Node(data)
        if not self.last:
            self.last = new_node
            new_node.next = self.last
        new_node.next = self.last.next
        self.last.next = new_node

    def remove(self) -> Any:
        if not self.last:
            return

        del_node = self.last
        
        if self.last == self.last.next:
            self.last = None
            return del_node.data

        tmp = self.last.next
        while tmp.next != self.last:
            tmp = tmp.next
        self.last = self.last.next
        tmp.next = self.last

        del_node.next = None
        del_node.prev = None
        return del_node.data

    def __str__(self) -> str:
        if not self.last:
            return '[]'

        res = ""
        template = "[{}] -> "
        tmp = self.last
        while tmp.next != self.last:
            res += template.format(tmp.data)
            tmp = tmp.next
        else:
            res += template.format(tmp.data)
        return res


if __name__ == "__main__":
    cll = CircularSingleLinkedList()
    for data in range(10):
        cll.append(data)
    print(cll)
    for _ in range(5):
        print(f'del: {cll.remove()}')
    print(cll)
