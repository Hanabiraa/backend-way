N = int(input())
prices = list(map(int, input().split()))



cols = 5
D = list([(0, 0, 0) for _ in range(N + 1)] for i in range(cols))

backtrack = list([(0, 0) for _ in range(N + 1)] for i in range(cols))

for i in range(N + 1):
    D[0][i] = (1, 0, 0)

# 1
D[1][1] = (0, 1 / prices[0], 0)

for j in range(2, N + 1):
    D[1][j] = (0, 1 / prices[j - 1], 0)
    # print(D[1][j])

    if D[1][j-1][1] > D[1][j][1]:
        D[1][j] = D[1][j-1]

# 2
last = D[1][1][1]
D[2][2] = (last * prices[1], 0, last * prices[1])

for j in range(3, N + 1):
    D[2][j] = (D[1][j - 1], 1 / prices[j - 1], 0)
    # print(D[1][j])

    if D[2][j-1][0] > D[2][j][0]:
        D[1][j] = D[1][j-1]

# 3
D[1][1] = (0, 1 / prices[0], 0)

for j in range(3, N + 1):
    D[1][j] = (0, 1 / prices[j - 1], 0)
    # print(D[1][j])

    if D[1][j-1][1] > D[1][j][1]:
        D[1][j] = D[1][j-1]

# 4

last = D[1][1][1]
D[2][2] = (last * prices[1], 0, last * prices[1])

for j in range(4, N + 1):
    D[2][j] = (D[1][j - 1], 1 / prices[j - 1], 0)
    # print(D[1][j])

    if D[2][j-1][0] > D[2][j][0]:
        D[1][j] = D[1][j-1]

print(D)

# backtrack