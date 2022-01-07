import random
from copy import deepcopy


def insertionSort_immutable(arr: tuple) -> tuple:
    """
    insertionSort for immutable collections
    average speed O(N^2)

    :param arr: tuple - immutable collection to sort
    :return: sorted new immutable collection in ascending

    i.e:
    >>> lst = -157, 174, 45, 62, -136
    >>> insertionSort_immutable(lst)
    (-157, -136, 45, 62, 174)
    """
    result = []
    if arr:
        for i in range(len(arr)):
            for j in range(len(result)):
                if result[j] >= arr[i]:
                    result.insert(j, arr[i])
                    break
            else:
                result.append(arr[i])
    return tuple(result)


def insertionSort_mutable(lst: list) -> None:
    """
    insertionSort for mutable collections, sort in ascending order
    average speed O(N^2)

    :param lst: list - mutable collection to sort
    :return: None

    i.e:
    >>> lst = [-2, -91, -192, 22, 114, -28, -77, -18, -174, 199]
    >>> insertionSort_mutable(lst)
    >>> print(lst)
    [-192, -174, -91, -77, -28, -18, -2, 22, 114, 199]
    """
    for i in range(1, len(lst)):
        j = i - 1
        while j >= 0 and lst[j] > lst[i]:
            lst[i], lst[j] = lst[j], lst[i]
            i -= 1
            j -= 1


if __name__ == '__main__':
    test_counts = 3
    test_size = 15
    all_cases = []
    all_cases_sort = []
    for count in range(test_counts):
        all_cases.append([random.randint(-200, 200) for _ in range(test_size)])
        test_size -= 5
    else:
        all_cases.append([random.randint(-200, 200) for _ in range(2)])
        all_cases_sort = [sorted(lst) for lst in all_cases]

    # sorts, return list
    print(insertionSort_immutable.__name__)
    for case, check_case in zip(map(tuple, deepcopy(all_cases)), map(tuple, all_cases_sort)):
        print(f"{insertionSort_immutable(case) == check_case}")

    # sorts, none return, change list in-place
    func_lst = [insertionSort_mutable]
    for func in func_lst:
        print(func.__name__)
        for case, check_case in zip(deepcopy(all_cases), all_cases_sort):
            func(case)
            print(f"{case == check_case}")
