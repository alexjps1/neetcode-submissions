class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                # we're left of the pivot
                if target > nums[mid] or target < nums[l]:
                    # go right
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # we're right of the pivot
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
