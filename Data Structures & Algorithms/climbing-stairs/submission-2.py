from math import comb
class Solution:
    def climbStairs(self, n: int) -> int:
        summe = 0
        for twosteps in range(n//2+1):
            onesteps = n - 2*twosteps
            summe += comb(onesteps + twosteps, onesteps)
        return summe


