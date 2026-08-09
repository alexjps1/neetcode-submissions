class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            addup = numbers[i] + numbers[j]
            if addup == target:
                return [i+1, j+1]
            if addup > target:
                j -= 1
            else:
                i += 1