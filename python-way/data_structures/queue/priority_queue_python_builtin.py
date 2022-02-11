from queue import PriorityQueue


def main():
    q = PriorityQueue()

    for val in range(0, 10):
        q.put(val)

    for val in range(10, 0, -1):
        q.put(val)

    for val in range(-10, 11, 2):
        q.put(val)

    while not q.empty():
        print(q.get(), end=' ')


if __name__ == '__main__':
    main()
