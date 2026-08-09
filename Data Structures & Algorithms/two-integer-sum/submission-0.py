class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a number:index mapping
        mymap = {}
        for index, number in enumerate(nums):
            if target - number in mymap:
                return [mymap[target - number], index]
            else:
                mymap[number] = index
            

