class Solution(object):
    def maximalSquare(self, matrix):
        # Edge case
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        # DP table with 1-cell padding
        T = [[0] * (n + 1) for _ in range(m + 1)]

        max_side = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Accept either ints (1/0) or strings ('1'/'0')
                if matrix[i - 1][j - 1] == 1 or matrix[i - 1][j - 1] == '1':
                    T[i][j] = min(T[i - 1][j], T[i][j - 1], T[i - 1][j - 1]) + 1
                    if T[i][j] > max_side:
                        max_side = T[i][j]
                else:
                    T[i][j] = 0

        # LeetCode asks for area of the largest square
        return max_side * max_side



        