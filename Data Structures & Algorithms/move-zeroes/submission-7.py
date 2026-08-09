class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
                j += 1
        return nums