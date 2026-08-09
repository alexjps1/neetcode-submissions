class MedianFinder:

    def __init__(self):
        self.nums = []
        self.length = 0
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort() # fix this for a more efficient approach
        self.length += 1
        

    def findMedian(self) -> float:
        if self.length % 2:
            # odd
            return self.nums[self.length // 2]
        return (self.nums[self.length//2-1] + self.nums[self.length//2]) /  2
        
        