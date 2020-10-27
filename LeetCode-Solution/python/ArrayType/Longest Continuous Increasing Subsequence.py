#674. Longest Continuous Increasing Subsequence
# Input: nums = [1,3,5,4,7]
# Output: 3

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        c = 1 #counts length of each sub sequence
        maxLength = 0 #maximum length
        for i in range(0, l - 1):
            if i+1 < len(nums) and nums[i] < nums[i+1]:
                c += 1
            else:
                if (c > maxLength):
                    maxLength = c
                c = 1
                
        if (c > maxLength):
            maxLength = c
            
        return maxLength