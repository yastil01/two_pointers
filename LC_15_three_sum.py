
***
Remember to sort the array if the input array is not already sorted
***

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        res = []
        n = len(nums) 
        for first in range(n):
            if first > 0 and nums[first] == nums[first-1]:
                continue
                
            second = first + 1
            third = n - 1
            while second < third:
                if nums[first] + nums[second] + nums[third] == 0:
                    res.append([nums[first], nums[second], nums[third]])
                    while second < third and nums[second] == nums[second+1]:
                        second += 1
                    second += 1
                    third -= 1
                elif nums[first] + nums[second] + nums[third] < 0:
                    second += 1
                else:
                    third -= 1
        
        return res
