class Solution(object):
    def reformatNumber(self, number):
        number = number.replace("-", "").replace(" ", "")
        res = []
        i = 0
        n = len(number)
        
        while n - i > 4:
            res.append(number[i:i+3])
            i += 3
        
        if n - i == 4:
            res.append(number[i:i+2])
            res.append(number[i+2:i+4])
        else:
            res.append(number[i:])
        
        return "-".join(res)