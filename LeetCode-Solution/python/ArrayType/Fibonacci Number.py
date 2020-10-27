#509. Fibonacci Number
#The Fibonacci numbers, commonly denoted F(n) form a sequence, 
#called the Fibonacci sequence, such that each number is the sum of the 
#two preceding ones, starting from 0 and 1. That is

class Solution:
    def fib(self, N: int) -> int:
            if N <= 1:
                return N
            return self.fib(N-1) + self.fib(N-2)