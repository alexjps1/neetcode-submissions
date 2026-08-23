class Solution:
    def isHappy(self, n: int) -> bool:
        prev = set()
        while n not in prev:
            prev.add(n)
            if n == 1:
                return True
            n = sum([int(i)**2 for i in str(n)])
        return False