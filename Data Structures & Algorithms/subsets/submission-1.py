class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for bitmap in range(0, (1 << n)):
            cur = []
            for i in range(n):
                if (bitmap >> i) & 1:
                    cur.append(nums[i])
            res.append(cur)
        return res




        