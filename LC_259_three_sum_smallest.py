class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        
        nums.sort()
        count = 0
        n = len(nums)
        for first in range(n):
            second = first + 1
            third = n - 1
            while second < third:
                if nums[first] + nums[second] + nums[third] < target:
                    count += third-second
                    second += 1
                else:
                    third -= 1
            
        return count   
