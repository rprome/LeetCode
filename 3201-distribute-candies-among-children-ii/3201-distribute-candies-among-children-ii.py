class Solution(object):
    def distributeCandies(self, n, limit):
        count = 0
        for i in range(0, min(limit, n) + 1):
            low = max(0, n - i - limit)
            high = min(limit, n - i)
            if low <= high:
                count += (high - low + 1)
        return count
