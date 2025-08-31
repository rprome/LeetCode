class Solution(object):
    def generateParenthesis(self, n):
        res = []

        def backtrack(cur, open_used, close_used):
            if open_used == n and close_used == n:
                res.append(cur)
                return

            if open_used < n:
                backtrack(cur + "(", open_used + 1, close_used)

            if close_used < open_used:
                backtrack(cur + ")", open_used, close_used + 1)

        backtrack("", 0, 0)
        return res
