class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        starters = []
        for i in nums:
            if i-1 not in numset:
                starters.append(i)
        
        best = 0
        for i in starters:
            ct = 1
            cur = i
            while cur+1 in numset:
                cur += 1
                ct += 1
            best = max(best, ct)
        
        return best

            

        

