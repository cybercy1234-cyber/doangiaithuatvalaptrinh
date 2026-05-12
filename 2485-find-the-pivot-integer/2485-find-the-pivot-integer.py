class Solution(object):
    def pivotInteger(self, n):
        total = n * (n + 1) // 2

        x = int(total ** 0.5)

        if x * x == total:
            return x
        else:
            return -1
                