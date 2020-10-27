# 485. Max Consecutive Ones
#Given a binary array, find the maximum number of 
#consecutive 1s in this array.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0 #counter 
        max = 0 #max of numbers of 1
        for n in nums: 
            if (n == 1):
                c+=1
            else:
                if(c>max):
                    max = c
        if (c >max):
            max = c
            
        return max