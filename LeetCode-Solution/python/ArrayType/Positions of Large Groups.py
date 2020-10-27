# 830.Positions of Large Groups
# In a string s of lowercase letters, these letters form consecutive groups of the same character.
# For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".
# A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].
# A group is considered large if it has 3 or more characters.
# Return the intervals of every large group sorted in increasing order by start index.
#Input: s = "abcdddeeeeaabbbcd"  Output: [[3,5],[6,9],[12,14]]
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        c = 1 #counter 
        result= []
        end = 0
        start = 0
        for i in range(0, len(s)):
            if i < len(s)-1 and s[i] == s[i+1]:
                c+=1
            else:
                if c >= 3:
                    end = i
                    start = i-c+1
                    result.append([start,end])
                c=1
            if i == len(s) - 1:
                if c >= 3:
                    end = i
                    start = i-c+1
                    result.append([start,end])
        if c>= 3 and c == len(s):
            result.append([0, len(s)-1])
        
        return result
