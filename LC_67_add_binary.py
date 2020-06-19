'''
https://leetcode.com/problems/add-binary/
Time Complexity = O(max(m,n))
Time Complexity = O(1)
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p1, p2  = len(a)-1, len(b)-1
        carry, res = 0, ""
        while p1 >= 0 or p2 >= 0 or carry:
            if p1 >= 0:
                carry += int(a[p1])
                p1 -= 1
            if p2 >= 0:
                carry += int(b[p2])
                p2 -= 1
            res = str(carry%2) + res
            carry //= 2
        return res
