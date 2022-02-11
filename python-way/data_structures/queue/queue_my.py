from typing import Any


class NoElementsInQueue(Exception):
    pass


class Queue():
    """
    My queue implementation
    (Also, this implementation is suitable as a cyclic queue)

    Example:
    >>> q = Queue()
    >>> for val in range(10):
    >>>    q.enqueue(val)
    >>> q.peek()
    0
    >>> print(q)
    Queue: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """

    def __init__(self) -> None:
        self.list = []
        self.len = 0

    def enqueue(self, val: Any) -> None:
        self.len += 1
        self.list.append(val)

    def dequeue(self) -> Any:
        if self.len:
            self.len -= 1
            return self.list.pop(0)
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
    q = Queue()
    for val in range(10):
        q.enqueue(val)
    print(q)
    print('Len: ', len(q))
    print('Pop: ', q.dequeue())
    print('After pop: ', q)
    print('Peek: ', q.peek())
    print('After peek: ', q)
    print('Is empty?: ', q.is_empty())

    print('First generator: ')
    for val in q:
        print(val, end=' ')

    print('\nSecond generator: ')
    for val in q:
        print(val, end=' ')
    print('\nOriginal queue:', q)

    print('call raise!')
    for _ in range(20):
        q.dequeue()


if __name__ == '__main__':
    main()
