class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) > 1:
            if stones[0] == stones[1]:
                stones = stones[2:]
            else:
                stones[0] -= stones[1]
                stones.pop(1)
            stones.sort(reverse=True)


        return 0 if len(stones) == 0 else stones[0]
