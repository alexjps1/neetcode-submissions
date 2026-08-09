class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) > 1:
            x = stones.pop(0)
            y = stones.pop(0)
            if x == y:
                continue
            x -= y
            
            # Edge cases
            if not stones or x >= stones[0]:
                stones.insert(0, x)
                continue
            if x <= stones[-1]:
                stones.append(x)
                continue
            
            # Binary search
            l = 0
            r = len(stones) - 1
            while l < r:
                mid = (l + r) // 2
                if stones[mid] >= x:
                    l = mid + 1
                else:
                    r = mid
            stones.insert(l, x)
                    
        return 0 if len(stones) == 0 else stones[0]
