class Solution(object):
    def generateParenthesis(self, n):
        res = []

        def backtrack(cur, openN, closeN):
            if openN == n and closeN == n:
                res.append(cur)
                return

            if openN < n:
                backtrack(cur + "(", openN + 1, closeN)

            if closeN < openN:
                backtrack(cur + ")", openN, closeN + 1)

        backtrack("", 0, 0)
        return res
