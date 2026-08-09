class MedianFinder:

    def __init__(self):
        self.nums = []
        self.length = 0
        

    def addNum(self, num: int) -> None:
        if self.length == 0:
            self.nums.append(num)
            self.length += 1
            return

        # use binary search for inserting numbers
        l = 0
        r = self.length - 1
        while l <= r:
            mid = (l + r) // 2
            if self.nums[mid] < num:
                r = mid - 1
            else:
                l = mid + 1
        # l is the first position where the list number is greater than num to insert
        # list.insert inserts right before that position
        self.nums.insert(l, num)
        self.length += 1
        

    def findMedian(self) -> float:
        if self.length % 2:
            # odd
            return self.nums[self.length // 2]
        return (self.nums[self.length//2-1] + self.nums[self.length//2]) /  2
        
        