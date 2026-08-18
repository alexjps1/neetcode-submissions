class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = list(enumerate(nums))
        nums.sort(key=lambda x: x[1])
        n = len(nums)
        i, j = 0, n-1
        mysum = nums[i][1] + nums[j][1]
        while mysum != target:
            if mysum < target:
                i += 1
            else:
                j -= 1
            mysum = nums[i][1] + nums[j][1]
        return sorted([nums[i][0], nums[j][0]])

            