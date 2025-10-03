# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # Store the next node
            curr.next = prev      # Reverse the current node's pointer
            prev = curr           # Move prev to the current node
            curr = next_node      # Move curr to the next node

        return prev  # p