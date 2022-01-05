import random


def simply_quicksort(lst: list) -> list:
    """
    ! WARNING: likely stack recursion overflow  
    ! WARNING: max recursion - O(n) 
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
    left = [x for x in lst if x < pivot]
    right = [x for x in lst if x >= pivot]

    return simply_quicksort(left) + [pivot] + simply_quicksort(right)


# TODO: create other quicksort implementations and test it
if __name__ == '__main__':
    test_counts = 3
    test_size = 15
    all_cases = []
    for count in range(test_counts):
        all_cases.append([random.randint(-200, 200) for _ in range(test_size)])
        test_size -= 5
    else:
        all_cases.append([random.randint(-200, 200) for _ in range(2)])

    for case in all_cases:
        print(f"before \t{case}")
        print(f"after \t{simply_quicksort(case)}\n")
