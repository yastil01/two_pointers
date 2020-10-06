class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return []
        
        map = {} # map to keep track of the last occurance index of each char
        for i in range(len(s)):
            map[s[i]] = i
        
        print(map)
        start = end = 0
        res = []
        for i in range(len(s)):
            end = max(end, map[s[i]])
            if i == end:
                res.append(end-start+1)
                start = end + 1
        
        return res
