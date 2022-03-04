"""
this module implement heap based on List and heapq module
"""
import heapq

if __name__ == "__main__":
    lst = [100, 10, 30, 20, 50, 40, 60, 90, 80, 70]
    
    print("lst before: {}".format(lst))
    heapq.heapify(lst)
    print("lst after heapify: {}".format(lst))
    heapq.heappush(lst, 110)
    print("lst after push: {}".format(lst))
    print("get 3 largest from heap: {}".format(heapq.nlargest(3, lst)))
    print("get 3 smallest from heap: {}".format(heapq.nsmallest(3, lst)))
    lst1 = [i for i in range(10)]
    merge_heap = list(heapq.merge(lst, lst1))
    print("lst after merge: {}".format(merge_heap))
    