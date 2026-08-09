# racing with simon, used help to make my solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        allnums = set(nums)
        for num in nums:
            if num -1 not in allnums:
                # it's a sequence starter
                length = 1
                while num+length in allnums:
                    length += 1
                longest = max(longest, length)
        return longest
                    
