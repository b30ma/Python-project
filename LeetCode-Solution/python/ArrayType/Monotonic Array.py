# 896. Monotonic Array
# Input: [1,2,2,3]   Output: true
# Input: [6,5,4,4]   Output: true
# Input: [1,3,2]     Output: false

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increasing = decreasing = True
        for i in range (0, len(A)):
            if i+1 < len(A):
                if A[i] > A[i+1]:
                    increasing = False
                if A[i] < A[i+1]:
                    decreasing = False

        return increasing or decreasing