def task(X, T, figs):
    end = T
    fig_dict = {
        idx: abs(X - size) for idx, size in enumerate(figs, start=1)
    }

    result = []
    for idx, size in sorted(fig_dict.items(), key=lambda pair: pair[1]):
        end -= size
        if end >= 0:
            result.append(idx)
        else:
            break

    return result


_, X, T = list(map(int, input().split()))
figs = list(map(int, input().split()))

result = task(X, T, figs)
print(len(result))
if result:
    print(*result)
