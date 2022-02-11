from collections import deque


def main():
    q = deque()
    for val in range(10):
        q.appendleft(val)
    for val in range(-10, 0):
        q.append(val)
    print(q)
    print('Pop: ', q.popleft(), q.pop())
    print(q)

if __name__ == '__main__':
    main()
