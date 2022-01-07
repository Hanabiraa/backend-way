import random
from copy import deepcopy


def mergeSort_top_to_down(lst: list) -> list:
    """
    mergesort top-to-down implementation
    average speed O(Nlog(N))

    :param lst: list - list to sort
    :return: list - sorted list in ascending

    i.e:
    >>> lst = [-157, 174, 45, 62, -136]
    >>> mergesort_top_to_down(lst)
    [-157, -136, 45, 62, 174]
    """
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = mergeSort_top_to_down(lst[:mid])
    right = mergeSort_top_to_down(lst[mid:])

    return list(_merge_for_top_to_down(left, right))


def _merge_for_top_to_down(left: list, right: list) -> int:
    """
    generator function for use in merge sort, 
    merge left and right lists in order by ascending

    :param left: list - list to merge
    :param right: list - list to merge
    :return: int (the element that is stored in these lists)
    """
    while left and right:
        yield (left if left[0] <= right[0] else right).pop(0)
    yield from (left if left else right)


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
    print(mergeSort_top_to_down.__name__)
    for case, check_case in zip(deepcopy(all_cases), all_cases_sort):
        print(f"{mergeSort_top_to_down(case) == check_case}")

    # sorts, none return, change list in-place
    # func_lst = []
    # for func in func_lst:
    #     print(func.__name__)
    #     for case, check_case in zip(deepcopy(all_cases), all_cases_sort):
    #         func(case, 0, len(case)-1)
    #         print(f"{case == check_case}")
