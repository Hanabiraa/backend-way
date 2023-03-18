N, X, T = map(int, input().split())

array = sorted(enumerate(map(int, input().split()), 1), key= lambda entry: abs(X - entry[1]))


# print(array)
ans = []

i = 0

while (T >= 0 and i < N and (delta:=abs(X - array[i][1])) <= T):

    if delta <= T:
        # print(T, delta, array[i])
        T -= delta
        ans.append(array[i][0])

    i += 1

print(len(ans))
print(*ans)