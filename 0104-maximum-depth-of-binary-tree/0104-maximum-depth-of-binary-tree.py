
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right= self.maxDepth(root.right)
            return 1 + (max(left, right))

   