class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        box = [0] * 46  # max tổng chữ số là 45

        for i in range(lowLimit, highLimit + 1):
            s = sum(int(d) for d in str(i))
            box[s] += 1

        return max(box)