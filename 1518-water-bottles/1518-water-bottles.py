class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        empty = 0
        total = 0

        while numBottles > 0:
            total += numBottles      # drink all full bottles
            empty += numBottles      # collect empty bottles

            numBottles = empty // numExchange  # exchange
            empty = empty % numExchange        # leftover empties

        return total