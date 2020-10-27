#268 -Given an array nums containing n distinct numbers in the range [0, n], 
# return the only 
# number in the range that is missing from the array.
#Follow up Q: 
    #Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
# bigO=nlog(n)
#class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         i = 0
#         nums.sort()
#         for n in nums:
#             if i != n:
#                 return i
#             i+=1
        
#         return i
#bigO = n
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        totalSum = (l * (l+1)) / 2
        sum = 0
        for n in nums:
            sum += n
        
        return int(totalSum) - sum