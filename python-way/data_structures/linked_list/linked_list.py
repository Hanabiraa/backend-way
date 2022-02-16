from typing import Any


class _Node():
    """
    Node builder for linked list implementation
    """

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList():
    """
    My implementation of simply linked list

    Example:
    >>> l = LinkedList()
    >>> for data in range(10):
    >>>     l.insert_right(data)
    >>> print(l)
    [0]->[1]->[2]->[3]->[4]->[5]->[6]->[7]->[8]->[9]
    """

    def __init__(self) -> None:
        self.head = None

    def insert_left(self, data: Any) -> None:
        new = _Node(data)
        new.next = self.head
        self.head = new

    def insert_right(self, data: Any) -> None:
        new = _Node(data)

        if not self.head:
            self.head = new
            return

        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = new

    def insert_after(self, prev_node: _Node, data: Any) -> None:
        new = _Node(data)
        if prev_node:
            new.next = prev_node.next
            prev_node.next = new
        else:
            new.next = self.head
            self.head = new

    def delete_left(self) -> Any:
        if self.head:
            delete = self.head
            self.head = self.head.next
            return delete.data
        return None

    def delete_right(self) -> Any:
        if self.head:
            tmp = self.head
            while tmp.next.next:
                tmp = tmp.next
            delete = tmp.next
            tmp.next = None
            return delete.data
        return None

    def delete_after(self, prev_node: _Node) -> Any:
        if prev_node:
            if delete := prev_node.next:
                prev_node.next = delete.next
                return delete.data
            else:
                return None
        return self.delete_left()

    def search(self, data: Any) -> Any:
        tmp = self.head
        while tmp:
            if tmp.data == data:
                return True
            tmp = tmp.next
        return False

    def _middle_el(self, head: _Node) -> _Node:
        slow_ptr = head
        fast_ptr = head.next
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr

    def _sortedMerge(self, left: _Node, right: _Node) -> _Node:
        sorted_seq = _Node(None)
        
        tmp = sorted_seq
        while left and right:
            if left.data < right.data:
                tmp.next = left
                left = left.next
            else:
                tmp.next = right
                right = right.next
            tmp = tmp.next
        
        while left:
            tmp.next = left
            left = left.next
            tmp = tmp.next
        
        while right:
            tmp.next = right
            right = right.next
            tmp = tmp.next
     
        return sorted_seq.next

    def _mergeSort(self, head: _Node) -> Any:
        if not head or not head.next:
            return head

        mid = self._middle_el(head)
        mid_next = mid.next
        mid.next = None

        left = self._mergeSort(head)
        right = self._mergeSort(mid_next)
        
        sorted_list = self._sortedMerge(left, right)
        return sorted_list

    def sort(self) -> None:
        self.head = self._mergeSort(self.head)

    def __str__(self) -> str:
        template = "[{}]->"
        full = ""
        tmp = self.head
        while tmp:
            full += template.format(tmp.data)
            tmp = tmp.next
        return full[:-2]


if __name__ == '__main__':
    l = LinkedList()

    for data in range(10):
        l.insert_right(data)
    for data in range(-10, 0):
        l.insert_left(data)

    tmp = l.head
    while tmp.next.next:
        tmp = tmp.next
    l.insert_after(tmp, 500)
    l.insert_after(None, -500)
    print("after insert:\n", l)

    l1 = LinkedList()
    for data in range(10):
        l1.insert_left(data)
    print("before: ", l1)
    print("delete_left: ", l1.delete_left())
    print("delete_right: ", l1.delete_right())
    print("after del: ", l1)

    tmp = l1.head
    while tmp.next.next:
        tmp = tmp.next
    print("delete after: None: ", l1.delete_after(None))
    print("delete after: tmp: ", l1.delete_after(tmp))
    print("tmp data: ", tmp.data)
    print("delete after: tmp x2: ", l1.delete_after(tmp))
    print(l1)

    print("search no occur: ", l1.search(200))
    print("search occur: ", l1.search(7))

    l1.sort()
    print(l1)
