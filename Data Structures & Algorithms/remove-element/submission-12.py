class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k is number of remaining
        j = len(nums) - 1
        i = 0
        while True:
            while j >= 0 and nums[j] == val:
                j -= 1
            if i >= j:
                return j + 1
            if val == nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            i += 1