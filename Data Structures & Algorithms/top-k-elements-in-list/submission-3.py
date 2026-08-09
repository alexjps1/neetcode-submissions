class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        buckets = [[] for i in range(len(nums)+1)]
        for num, frequency in counts.items():
            buckets[frequency].append(num)
        print(buckets)
        top_k = []
        pos = -1
        while len(top_k) < k:
            top_k += buckets[pos]
            pos -= 1
        return top_k[:k]            



    