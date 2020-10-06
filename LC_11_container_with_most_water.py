class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        
        leftMax = rightMax = float('-inf')
        left, right = 0, len(height) - 1
        maxArea = currArea = 0
        
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            currArea = (right - left) * min(leftMax,rightMax)
            maxArea = max(maxArea, currArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return maxArea 
