class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        t = sorted(list(zip(names, heights)), key = lambda x: -x[1])
        return [i[0] for i in t]
        