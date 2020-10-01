class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return -1
       
        nums.sort() 
        res = minDiff = float('inf')
        n = len(nums)
        for first in range(n):
            second = first + 1
            third = n - 1
            while second < third:
                currSum = nums[first] + nums[second] + nums[third]
                if currSum == target:
                    return currSum
                elif currSum < target:
                    second += 1
                else:
                    third -= 1
                
                if abs(currSum - target) < minDiff:
                    minDiff = abs(currSum - target)
                    res = currSum
        
        return res
