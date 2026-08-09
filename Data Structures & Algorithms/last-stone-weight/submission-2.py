# annotations of the optimal bucket sort solution

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create bucket sort buckets
        # weight = bucket, so each bucket is frequency of stones w that weight
        maxweight = max(stones)
        bucket = [0] * (maxweight + 1)
        for stone in stones:
            bucket[stone] += 1
        
        # pointers for heaviest and second heaviest stone
        p1 = p2 = maxweight

        while p1 > 0:
            # even number of same-weight stones cancel out
            if bucket[p1] % 2 == 0:
                p1 -= 1
                continue
            
            # odd number: all but one cancel out
            # use j to find p2 so we can smash p1 and p2
            j = min(p1 - 1, p2)
            while j > 0 and bucket[j] == 0:
                j -= 1
            
            # last stone if the second pointer doesn't find any other stones
            if j == 0:
                return p1
            p2 = j

            # move heavier stone to its new weight
            bucket[p1] -= 1 
            bucket[p1 - p2] += 1

            # lighter stone always loses, remove it
            bucket[p2] -= 1 

            # new heaviest is eighter previous p2 or the newly-made p1 - p2 stone
            p1 = max(p1 - p2, p2)
        
        return p1 # because in the bucket sort, index = weight
