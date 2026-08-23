class Solution:
    def sumOfSquares(self, n: int) -> int:
        res = 0
        while n:
            digit = n % 10
            res += digit**2
            n = n // 10
        return res

    def isHappy(self, n: int) -> bool:
        s = n
        f = self.sumOfSquares(n)
        phase = 2
        phaseprog = 0
        while s != f:
            if phaseprog == phase:
                s = self.sumOfSquares(s)
                phase = phase * 2
                phaseprog = 0
            f = self.sumOfSquares(f)
            phaseprog += 1
            if f == 1 or s == 1:
                return True
        return False if s != 1 else True
        
            
        

