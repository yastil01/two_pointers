"""
simple two pointer
corner case: ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
ans: ab12
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        
        start = index = 0
        for end in range(len(chars)+1):
            if end == len(chars) or chars[end] != chars[start]:
                chars[index] = chars[start]
                index += 1
                freq = end -start
                if freq > 1:
                    for c in str(freq):
                        chars[index] = c
                        index += 1
                start = end
        
        return index
