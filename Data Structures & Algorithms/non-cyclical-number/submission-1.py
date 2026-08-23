class Solution:
    def sumOfSqures(self, n: int) -> int:
        res = 0
        while n:
            digit = n % 10
            res += digit**2
            n = n // 10
        return res

    def isHappy(self, n: int) -> bool:
        prev = set()
        while n not in prev:
            prev.add(n)
            if n == 1:
                return True
            n = self.sumOfSqures(n)
        return False