#219- Given an array of integers and an integer k, 
# find out whether there are two distinct indices i and j in the array 
# such that nums[i] = nums[j] and the 
# absolute difference between i and j is at most k.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        i = 0
        for n in nums:
            if n in dic: 
                if i - dic[n] <= k:
                    return True
                else:
                    dic[n] = i
            else: 
                dic[n]=i
            i += 1
        
        return False