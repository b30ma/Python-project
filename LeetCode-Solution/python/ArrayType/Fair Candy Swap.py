# 888. Fair Candy Swap
# Input: A = [1,1], B = [2,2]
# Output: [1,2]
# Algorithm :
# S.A−x+y=S  S.B=−y+x
# y= x + (S.B - S.A)/2

​class Solution(object):
    def fairCandySwap(self, A, B):
        Sa, Sb = sum(A), sum(B)
        setB = set(B)
        for x in A:
            if x + (Sb - Sa) / 2 in setB:
                return [x, x + (Sb - Sa) / 2]