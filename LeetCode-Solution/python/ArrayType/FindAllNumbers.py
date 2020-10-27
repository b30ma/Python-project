#448-Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        res = []
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        for i in range(1,len(nums)+1):
            if not(i in dic):
                res.append(i)
        
        return res