***
Remember to sort the array if the input array is not already sorted
***
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        
        nums.sort() 
        maxSum = nums[0]
        left , right = 0, len(nums)-1
        while left < right:
            if nums[left] + nums[right] < k:
                maxSum = max(maxSum, nums[left] + nums[right])
                left += 1
            else:
                right -= 1
        
        if maxSum == nums[0]:
            return -1
        return maxSum
