class Solution:
    def eat(self, piles: List[int], k: int) -> int:
        # return time it takes to eat (compare to k later)
        return sum([math.ceil(pile / k) for pile in piles])

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) 
        # insert position version of bin search (i.e. earliest l that satisfies)
        while l < r:
            mid = (l + r) // 2
            h_taken = self.eat(piles, k=mid)
            if h_taken > h:
                l = mid + 1
            else:
                r = mid
        return l 

