class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        ct = 0
        i = -1
        while i < l - 1:
            if sum(flowerbed[max(0, i):min(l, i+3)]) == 0:
                ct += 1
                i += 1
            i += 1
        return ct >= n
            
            
        