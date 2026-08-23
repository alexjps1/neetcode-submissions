class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heap = [-math.inf] * k
        for i in range(len(nums)):
            if nums[i] > heap[0]:
                heapq.heapreplace(heap, nums[i])
        self.heap = heap

    def add(self, val: int) -> int:
        if not self.heap:
           self.heap.append(val) 
        if val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
        
