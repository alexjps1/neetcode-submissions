class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxim = nums[0]
        summe = 0
        for num in nums:
            if summe < 0:
                summe = 0
            summe += num
            maxim = max(maxim, summe)
        return maxim



