class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        buckets = [[] for i in range(len(nums)+1)]
        for num, frequency in counts.items():
            buckets[frequency].append(num)
        top_k = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k
        return top_k