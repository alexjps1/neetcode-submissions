class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.res = []

        def dfs(i, curList, total):
            if total == target:
                self.res.append(curList.copy())
                return
            if total > target:
                return
            for j in range(i, len(nums)):
                curList.append(nums[j])
                dfs(j, curList, total + nums[j])
                curList.pop()
        
        dfs(0, [], 0)
        return self.res



