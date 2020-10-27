#724. Find Pivot Index
#Input: nums = [1,7,3,6,5,6]   Output: 3
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumL = 0
        sumR = sum(nums)
        for i in range(len(nums)):
            sumR -= nums[i]
            if sumL == sumR:
                return i
            sumL += nums[i]
        return -1