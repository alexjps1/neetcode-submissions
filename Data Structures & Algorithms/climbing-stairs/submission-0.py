from math import comb

class Solution:
    def climbStairs(self, n: int) -> int:
        summe = 0
        for twosteps in range(n//2+1):
            onesteps = n - 2*twosteps
            print(f"onesteps: {onesteps}, twosteps: {twosteps}")
            if onesteps != 0:
                combi = comb(onesteps + twosteps, onesteps)
                print(f"    possible combinations: {combi}")
                summe += combi
            else:
                print("    possible combinations: 1")
                summe  += 1
        print(f"sum is {summe}")
        return summe


