class Solution:
    def threeSum(self, nums: List[int], target) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        res = []
        for first in range(len(nums)-2):
            if first == 0 or (first > 0 and nums[first] != nums[first-1]):
                second = first + 1
                third = len(nums) - 1
                while second < third:
                    sum = nums[first] + nums[second] + nums[third]
                    if sum == target:
                        res.append([nums[first], nums[second], nums[third]])
                        while second < third and nums[second] == nums[second +1]:
                            second += 1
                        second += 1
                        third -= 1
                    elif sum < target:
                        second += 1
                    else:
                        third -= 1
        
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        
        nums.sort()
        res = []
        for first in range(len(nums)-3):
            if first == 0 or (first > 0 and nums[first] != nums[first-1]):
                resThreeSum = self.threeSum(nums[first+1:], target-nums[first])
                for item in resThreeSum:
                    res.append([nums[first]]+item)
        
        return res
