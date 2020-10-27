# 977. Squares of a Sorted Array
# Input: [-4,-1,0,3,10]  Output: [0,1,9,16,100]

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
           return sorted(x*x for x in A)