class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return False
       
        left , right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s[left+1:right+1]) or self.isPalindrome(s[left:right])
            left += 1
            right -= 1
        
        return True
            
    def isPalindrome(self, s):
        if not s:
            return True
        
        left, right = 0, len(s) -1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
