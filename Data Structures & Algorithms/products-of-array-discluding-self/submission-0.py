class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [None] * len(nums) 
        pre[0] = nums[0]
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i]

        post = [None] * len(nums) 
        post[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            post[i] = post[i+1] * nums[i]
        
        output = [None] * len(nums)
        output[0] = post[1]
        output[-1] = pre[-2]
        for i in range(1, len(nums) -1):
            output[i] = pre[i-1] * post[i+1]
        
        return output
        

        

