class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sum = 0
        res = ''
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1 >= 0 or p2 >= 0 or sum:
            if p1 >= 0:
                sum += int(num1[p1])
                p1 -= 1
            if p2 >= 0:
                sum += int(num2[p2])
                p2 -= 1
            res = str(sum%10) + res
            sum = sum // 10
        
        return res
