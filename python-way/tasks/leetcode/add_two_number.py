# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result_ = []
    while l1 and l2:
        result_.append(l1.val + l2.val)
        l1 = l1.next
        l2 = l2.next

    last_seq = l1 if l1 else l2
    while last_seq:
        result_.append(last_seq.val)
        last_seq = last_seq.next

    flag = False
    for idx, num in enumerate(result_):
        if flag:
            num += 1
            flag = False

        if num >= 10:
            num -= 10
            flag = True
        result_[idx] = num

    if flag:
        result_.append(1)

    head = ListNode(result_[0])
    ptr = head
    for num in result_[1:]:
        ptr.next = ListNode(num)
        ptr = ptr.next

    return head


def main():
    # l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    # l2 = ListNode(5, ListNode(6, ListNode(4, None)))

    l1 = ListNode(
        9, ListNode(
            9, ListNode(
                9, ListNode(
                    9, ListNode(
                        9, ListNode(
                            9, ListNode(
                                9, None)))))))
    l2 = ListNode(
        9, ListNode(
            9, ListNode(
                9, ListNode(
                    9, None))))

    # l1 = ListNode(0, None)
    # l2 = ListNode(0, None)

    result = addTwoNumbers(l1, l2)

    # print(result)
    while result:
        print(result.val)
        result = result.next


if __name__ == '__main__':
    main()
