# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        visited = {}         
        curr = head

        while curr:
            if curr in visited:   
                return True
            visited[curr] = True  
            curr = curr.next

        return False      