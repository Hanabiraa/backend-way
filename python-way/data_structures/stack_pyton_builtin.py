from queue import LifoQueue # 1 implementation
from collections import deque # 2 implementation (i think its best)

def main():
    stack = LifoQueue()
    for val in range(10):
        stack.put(val)
    for _ in range(10):
        print(stack.get(), end=' ')
    print('\n\n\n')

    stack1 = deque()
    print(stack1)
    for val in range(10):
        stack1.append(val)
    print(stack1)
    for _ in range(10):
        stack1.pop()
    print(stack1)
    print(len(stack1))
    stack1.pop()

if __name__ == '__main__':
    main()
