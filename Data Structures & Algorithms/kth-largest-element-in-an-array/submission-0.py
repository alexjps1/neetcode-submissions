class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = nums[:k]
        heapq.heapify(l)
        for i in nums[k:]:
            if i > l[0]:
                l[0] = i
                heapq.heapreplace(l, i)
        return l[0]