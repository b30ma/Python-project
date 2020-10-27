#665. Non-decreasing Array
#Input: nums = [4,2,3]
#Output: true
#Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        i = 0
        c = None #counter
        for n in range(len(nums)- 1):
            if nums[i] >= nums[i + 1]:
                
                if c is not None:
                    return False
                c = i
        return (c in None or c == 0 or c == len(nums)-2 or
                nums[c-1]<= nums(c+1) or nums[c] <= nums[c+2])
        