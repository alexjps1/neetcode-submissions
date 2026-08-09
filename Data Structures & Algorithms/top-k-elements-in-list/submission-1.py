class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = defaultdict(int)
        for num in nums:
            ct[num] += 1
        frequencies = list(ct.items())
        frequencies.sort(key=lambda x: x[1], reverse=True)
        return [i[0] for i in frequencies[:k]]
        