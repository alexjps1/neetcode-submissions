class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        myset = set()
        for num in nums:
            myset.add(num)
        i = 1
        while True:
            if i not in myset:
                return i
            i += 1
                
