from typing import Any


class NoElementsInQueue(Exception):
    pass


class Dequeue():
    """
    My dequeue implementation

    Example:
    >>> q = Dequeue()
    >>> for val in range(10):
    >>>    q.push_front(val)
    >>> for val in range(-10, 0):
    >>>    q.push_back(val)
    >>> print(q)
    Queue: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
    """

    def __init__(self) -> None:
        self.list = []
        self.len = 0

    def push_back(self, val: Any) -> None:
        self.len += 1
        self.list.append(val)

    def push_front(self, val: Any) -> None:
        self.len += 1
        self.list.insert(0, val)

    def pop_front(self) -> Any:
        if self.len:
            self.len -= 1
            return self.list.pop(0)
        else:
            raise NoElementsInQueue

    def pop_back(self) -> Any:
        if self.len:
            self.len -= 1
            return self.list.pop()
        else:
            raise NoElementsInQueue

    def is_empty(self) -> bool:
        return not bool(self.len)

    def peek(self) -> Any:
        return self.list[0]

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
    q = Dequeue()
    for val in range(10):
        q.push_front(val)
    for val in range(-10, 0):
        q.push_back(val)
    print(q)
    print('Pop: ', q.pop_front(), q.pop_back())
    print(q)

if __name__ == '__main__':
    main()
