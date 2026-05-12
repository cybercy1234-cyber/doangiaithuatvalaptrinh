class Solution(object):
    def divideArray(self, nums):
        
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for value in count.values():

            if value % 2 != 0:
                return False

        return True
        