class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s)-1
        map = set('aeiouAEIOU')
        while left < right:
            if s[left] in map and s[right] in map:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            else:
                if s[left] not in map:
                    left += 1
                if s[right] not in map:
                    right -= 1
        
        return ''.join(s)
