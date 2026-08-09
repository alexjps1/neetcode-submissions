class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = {}
        for num in nums:
            if ct.get(num) is not None:
                ct[num] += 1
            else:
                ct[num] = 1
        frequencies = list(ct.items())
        frequencies.sort(key=lambda x: x[1], reverse=True)
        return [i[0] for i in frequencies[:k]]
        