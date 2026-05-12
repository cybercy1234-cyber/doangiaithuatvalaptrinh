class Solution(object):
    def largestAltitude(self, gain):
        max=0
        s=0
        for i in gain:
            s=s+i
            if s>max:
                max=s
        
        return max