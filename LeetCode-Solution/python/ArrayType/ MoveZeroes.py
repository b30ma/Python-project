#283- Given an array nums, write a function to move all 0's to 
#the end of it while maintaining the relative order of the non-zero elements.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 """counter of 0"""
        j = 0 """pointer"""
        while (j < len(nums)):
            if nums[j] == 0:
                nums.remove(0)
                i+=1
            else: 
                j+=1
        while i > 0:
            nums.append(0)
            i-=1
        return nums       