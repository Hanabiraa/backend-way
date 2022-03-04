"""
My heap implementation based on list
"""

from typing import Iterable, List, Collection, Optional, Any
import operator


class Heap():
    """
    My heap implementation based on List

    Example:
    >>> lst1 = [94, 3, 2, 1, 15, 5, 4, 45, 60]
    >>> h_min = Heap(lst1, True)
    >>> print("heap (min): ", h_min)
    heap (min):  [1, 3, 2, 45, 15, 5, 4, 94, 60]
    """
    def __init__(self, data: List = [], min_heap=False) -> None:
        """
        heap_mode_operator - comparasion operator for heapify method
        """
        self.data: Collection = data.copy()
        self.__heap_mode_operator = (operator.lt if min_heap else operator.gt)
        Heap.heapify(self)

    def __str__(self) -> str:
        return str(self.data)

    def heapify(self) -> None:
        """
        start heapify from max right non-leaf node:
        index max_right_non_leaf = size//2-1
        """
        size = len(self.data)
        for p_node_index in range(size // 2 - 1, -1, -1):
            self.__heapify(size, p_node_index)

    def __heapify(self, size: int, p_node: int) -> None:
        """
        if i = parent node, then:
            2*i+1 - left child node
            2*i+2 - right child node
        """
        l_node = 2 * p_node + 1
        r_node = 2 * p_node + 2

        largest = p_node
        if l_node < size and self.__heap_mode_operator(self.data[l_node], self.data[largest]):
            largest = l_node
        if r_node < size and self.__heap_mode_operator(self.data[r_node], self.data[largest]):
            largest = r_node

        if p_node != largest:
            self.data[p_node], self.data[largest] = self.data[largest], self.data[p_node]
            self.__heapify(size, largest)

    def insert_heap(self, collection: Iterable) -> None:
        if collection:
            self.data.extend(collection)
            self.heapify()

    def insert_val(self, collection: Any) -> None:
        self.data.append(collection)
        self.heapify()

    def delete(self, val: Any) -> Any:
        if val in self.data:
            idx = self.data.index(val)
            del_val = self.data.pop(idx)
            self.heapify()
            return del_val
        return None

    def peek(self) -> Any:
        """
        result depend on heap type.
        return min/max value for Heap
        """
        return self.data[0]


if __name__ == "__main__":
    lst1 = [94, 3, 2, 1, 15, 5, 4, 45, 60]
    h_min = Heap(lst1, True)
    print("list: ", lst1)
    print("heap (min): ", h_min)

    h_max = Heap(lst1, min_heap=False)
    print("heap (max): ", h_max)

    lst3 = [1, 2, 3]
    lst4 = [9, 8, 7]
    merge_h = Heap()
    merge_h.insert_heap(lst3)
    print("Merge heap after 1st list: ", merge_h)
    merge_h.insert_heap(lst4)
    print("Merge heap after 2nd list: ", merge_h)
    merge_h.insert_val(50)
    print("Merge heap after insert val(50): ", merge_h)
    
    lst5 = [100, 10, 30, 20, 50, 40, 60, 90, 80, 70]
    h_for_del = Heap(lst5)

    print("heap before del: ", h_for_del)
    for data in [100, 30, 60, 70, 40]:
        print("del data: {}, heap: {}".format(h_for_del.delete(data), h_for_del))
