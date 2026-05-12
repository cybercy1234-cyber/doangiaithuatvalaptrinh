class Solution(object):
    def arrangeCoins(self, n):
        l = 0
        r = n
        ans = 0

        while l <= r:

            mid = (l + r) // 2

            if mid * (mid + 1) // 2 <= n:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans