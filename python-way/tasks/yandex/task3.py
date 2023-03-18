from pprint import pprint


def task(N, prices):
    days = {day: [] for day in range(N)}
    buy_id = 0
    while buy_id < N:
        buy = prices[buy_id]
        for sell_id, sell in enumerate(prices[buy_id:], start=buy_id):
            if (profit := sell - buy) > 0:
                days[buy_id].append([sell_id, profit])
        buy_id += 1

    pprint(days)
    result = []
    # max paths for 2 edges in graph
    for buy_day in days.keys():
        for sell_day1, profit1 in days[buy_day]:
            if sell_day1 + 1 >= N - 1:
                result.append([1, [buy_day + 1, sell_day1 + 1], [], profit1])
                break
            next_buy_day = days[sell_day1 + 1]
            if next_buy_day:
                sell_day2, profit2 = max(next_buy_day, key=lambda x: x[1])
                result.append([2, [buy_day + 1, sell_day1 + 1], [sell_day1 + 2, sell_day2 + 1], profit1 + profit2])
    pprint(result)
    return max(result, key=lambda x: x[3])[:3] if result else [0, [], []]


"""
5
2 5 2 1 4
"""
N = int(input())
prices = list(map(int, input().split()))
result = task(N, prices)

match result[0]:
    case 0:
        print(0)
    case 1:
        print(1)
        print(*result[1])
    case 2:
        print(2)
        print(*result[1])
        print(*result[2])
