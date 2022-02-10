class NoElementInStack(Exception):
    pass


class Stack():
    """
    My stack implementation

    Example:
    >>> stack = Stack()
    >>> stack.push(1)
    >>> len(stack)
    1
    >>> stack.pop()
    1
    """
    def __init__(self) -> None:
        self.list = []
        self.len = 0

    def push(self, val: object) -> None:
        self.list.append(val)
        self.len += 1

    def pop(self) -> object:
        if self.len:
            self.len -= 1
            return self.list.pop()
        else:
            raise NoElementInStack

    def is_empty(self) -> bool:
        return bool(self.len)

    def peek(self) -> object:
        return self.list[-1]

    def __repr__(self) -> str:
        return''.join(['Stack: ', str(self.list)])

    def __len__(self) -> int:
        return self.len

    def __iter__(self) -> object:
        while self.len:
            yield self.pop()


def main():
    stack = Stack()
    print(stack)
    for i in range(1, 6):
        stack.push(i)
    print(stack)
    print('Stack len: ', len(stack))
    print('Pop: ', stack.pop())
    print('Pop: ', stack.pop())
    print('Pop: ', stack.pop())
    print(stack)
    print('Stack len: ', len(stack))
    print('Pop: ', stack.pop())
    print('Pop: ', stack.pop())
    # print('Now raise!!! ', stack.pop())

    stack1 = Stack()
    for i in range(10):
        stack1.push(i)

    print('Generator object from Stack:')
    print('Stack len: ', len(stack1))
    print(*stack1)
    print('Stack len: ', len(stack1))


if __name__ == '__main__':
    main()
