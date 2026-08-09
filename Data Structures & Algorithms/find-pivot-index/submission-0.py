class Solution: 
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        running = 0
        for i in range(len(nums)):
            if total - nums[i] -  running == running:
                return i
            running += nums[i]
        return -1
        