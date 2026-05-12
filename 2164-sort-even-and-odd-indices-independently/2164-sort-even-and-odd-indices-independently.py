class Solution(object):
    def sortEvenOdd(self, nums):
        even = []
        odd = []

        # tách phần tử
        for i in range(len(nums)):

            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])

        # sắp xếp
        even.sort()
        odd.sort(reverse=True)

        e = 0
        o = 0

        # gán lại
        for i in range(len(nums)):

            if i % 2 == 0:
                nums[i] = even[e]
                e += 1
            else:
                nums[i] = odd[o]
                o += 1

        return nums


        