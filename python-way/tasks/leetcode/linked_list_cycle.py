# link -> https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # bad solution
        node_id = set()
        while head:
            if id(head) in node_id:
                return True
            node_id.add(id(head))
            head = head.next
        return False

    def _hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd’s Cycle Detection Algorithm
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
        