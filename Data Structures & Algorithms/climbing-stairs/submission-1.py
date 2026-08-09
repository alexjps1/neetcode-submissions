from math import comb

class Solution:
    def climbStairs(self, n: int) -> int:
        summe = 0
        for twosteps in range(n//2+1):
            onesteps = n - 2*twosteps
            combi = comb(onesteps + twosteps, onesteps)
            summe += combi
        print(f"sum is {summe}")
        return summe


