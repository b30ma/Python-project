#169-Given an array of size n, find the majority element. 
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element 
# always exist in the array.



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         majority_count = len(nums)//2
         for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num