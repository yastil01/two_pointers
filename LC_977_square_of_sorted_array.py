class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return []
       
        if len(A) == 1:
            return [A[0] * A[0]]
        
        pos = 0
        while A[pos] < 0: 
            pos += 1
        
        neg = pos-1 
        res = []
        while neg >= 0 and pos < len(A):
            sNeg = A[neg]*A[neg]
            sPos = A[pos]*A[pos]
            if sNeg < sPos:
                res.append(sNeg)
                neg -= 1
            else:
                res.append(sPos)
                pos += 1
        
        while neg >= 0:
            sNeg = A[neg]*A[neg]
            res.append(sNeg)
            neg -= 1
       
        while pos < len(A):
            sPos = A[pos]*A[pos]
            res.append(sPos)
            pos += 1
            
        return res
