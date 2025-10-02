# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        # Edge case: if there is only one node, return None
        if not head or not head.next:
            return None

        fast = head
        slow = head
        prev = None  # keep track of node before slow

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # now slow is at the middle, prev is the node before slow
        prev.next = slow.next  # delete the middle

        return head
