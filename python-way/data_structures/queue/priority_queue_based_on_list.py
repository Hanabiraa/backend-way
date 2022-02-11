from typing import Any


class NoElementsInQueue(Exception):
    pass


class PriorityQueue():
    """
    My priority queue implementation
    (based on list)

    Example:
    >>> q = PriorityQueue()
    >>> for val in range(0, 10):
    >>>    q.enqueue2(val)
    >>> print(q)
    Queue: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """

    def __init__(self) -> None:
        self.list = []
        self.len = 0

    def enqueue(self, val: Any) -> None:
        """
        very native
        """
        self.len += 1
        for idx, val_ in enumerate(self.list):
            if val <= val_:
                self.list.insert(idx, val)
                break
        else:
            self.list.append(val)

    def enqueue1(self, val: Any) -> None:
        """
        with binary search recursive
        """
        def bin_search(lst, low, high, val):
            if low > high:
                return low

            mid = (low + high) // 2
            if val > lst[mid]:
                return bin_search(lst, mid + 1, high, val)
            elif val < lst[mid]:
                return bin_search(lst, low, mid - 1, val)
            return mid

        id_ = bin_search(self.list, 0, self.len-1, val)
        self.len += 1
        self.list.insert(id_, val)

    def enqueue2(self, val: Any) -> None:
        """
        with binary search loop
        """

        mid = 0
        left = 0
        right = self.len - 1
        while left <= right:
            mid = (left + right) // 2
            if val == self.list[mid]:
                break
            elif val > self.list[mid]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            mid = left

        self.len += 1
        self.list.insert(mid, val)

    def dequeue(self) -> Any:
        if self.len:
            self.len -= 1
            return self.list.pop(0)
        else:
            raise NoElementsInQueue

    def __repr__(self) -> str:
        return''.join(['Queue: ', str(self.list)])

    def __len__(self) -> int:
        return self.len

    def __iter__(self) -> object:
        """
        original queue not used
        """
        def gen(lst: list) -> object:
            yield from lst
        return gen(self.list)


def main():
    q = PriorityQueue()
    for val in range(0, 10):
        q.enqueue2(val)
    print(q)

    for val in range(10, 0, -1):
        q.enqueue2(val)
    print(q)

    for val in range(-10, 11, 2):
        q.enqueue2(val)
    print(q)


if __name__ == '__main__':
    main()
