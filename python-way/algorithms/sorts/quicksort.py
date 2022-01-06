import random
from copy import deepcopy


def quicksort_simply(lst: list) -> list:
    """
    ! WARNING: likely stack recursion overflow  
    ! WARNING: max recursion - O(N) 
    ! WARNING: removes one element from the original list. 
    ! If you need original list - use .copy()

    simple quicksort implementation, average speed O(Nlog(N))
    :param lst: list - list to sort
    :return: sorted list in ascending

    i.e:
    >>> simply_quicksort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """

    if not lst:
        return []

    pivot = lst.pop()
    less = []
    more = []

    for x in lst:
        (less if x < pivot else more).append(x)
    return quicksort_simply(less) + [pivot] + quicksort_simply(more)


def quicksort_Lomuto(lst: list, low: int, high: int) -> None:
    """
    quicksort implementation with Lomuto partition, change list in place
    average speed O(Nlog(N))

    :param lst: list - list to sort
    :param low: first index of list
    :param high: last index of list
    :return: none

    i.e:
    >>> lst = [-2, -91, -192, 22, 114, -28, -77, -18, -174, 199]
    >>> quicksort_Lomuto(lst, 0, len(lst) - 1)
    >>> print(lst)
    [-192, -174, -91, -77, -28, -18, -2, 22, 114, 199]
    """
    if low < high and low >= 0:
        idx: int = _quicksort_Lomuto_partition(lst, low, high)
        quicksort_Lomuto(lst, low, idx-1)
        quicksort_Lomuto(lst, idx+1, high)


def _quicksort_Lomuto_partition(lst: list, low: int, high: int) -> int:
    """
    Lomuto partition func for quicksort algorithm

    :param lst: list - list to sort
    :param low: first index of list
    :param high: last index of list
    :return: pivot index 
    (pivot - the element with which all other elements of the list are compared)
    """
    pivot = lst[high]
    i = low
    for j in range(low, high):
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    else:
        lst[i], lst[high] = lst[high], lst[i]
        
    return i


def quicksort_Hoare(lst: list, low: int, high: int) -> None:
    """
    quicksort implementation with Hoare partition, change list in place
    average speed O(Nlog(N))

    :param lst: list - list to sort
    :param low: first index of list
    :param high: last index of list
    :return: none

    i.e:
    >>> lst = [-2, -91, -192, 22, 114, -28, -77, -18, -174, 199]
    >>> quicksort_Hoare(lst, 0, len(lst) - 1)
    >>> print(lst)
    [-192, -174, -91, -77, -28, -18, -2, 22, 114, 199]
    """
    if low >= 0 and high >= 0 and low < high:
        idx: int = _quicksort_Hoare_partition(lst, low, high)
        quicksort_Lomuto(lst, low, idx)
        quicksort_Lomuto(lst, idx+1, high)


def _quicksort_Hoare_partition(lst: list, low: int, high: int) -> int:
    """
    Hoare partition func for quicksort algorithm

    :param lst: list - list to sort
    :param low: first index of list
    :param high: last index of list
    :return: last index
    (pivot - the element with which all other elements of the list are compared)
    """
    pivot: lst[int] = lst[(low + high) // 2]
    while low >= high:
        while lst[low] < pivot:
            low += 1
        while lst[high] > pivot:
            high -= 1
        else:
            lst[low], lst[high] = lst[high], lst[low]
    return high


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

    # special loop, because return list
    print(quicksort_simply.__name__)
    for case, check_case in zip(deepcopy(all_cases), all_cases_sort):
        print(f"{quicksort_simply(case) == check_case}")

    # none return, change list in-place
    func_lst = [quicksort_Lomuto, quicksort_Hoare]
    for func in func_lst:
        print(func.__name__)
        for case, check_case in zip(deepcopy(all_cases), all_cases_sort):
            func(case, 0, len(case)-1)
            print(f"{case == check_case}")
