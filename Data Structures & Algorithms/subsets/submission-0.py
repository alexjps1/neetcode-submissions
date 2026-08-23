class Solution:
    def pick_next(self, existing: List[int], candidate_idx: int):
        self.pool.append(existing)
        for i in range(candidate_idx, self.n):
            new_candidate_idx = i + 1
            candidate = self.nums[i]
            self.pick_next(existing + [candidate], new_candidate_idx)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.n = len(nums)
        self.nums = nums
        self.pool = []
        self.pick_next([], 0)
        return self.pool


        