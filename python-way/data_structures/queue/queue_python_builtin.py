from queue import Queue


def main():
    q = Queue()
    for val in range(10):
        q.put(val)

    print('Queue: ', end='')
    for _ in range(10):
        print(q.get(), end=' ')


if __name__ == '__main__':
    main()
