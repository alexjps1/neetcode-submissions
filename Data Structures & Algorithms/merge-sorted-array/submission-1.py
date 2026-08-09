class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 # nums1
        j = n - 1# nums2
        for cur in range(len(nums1)-1, -1, -1):
            if i < 0:
                use1 = False
            elif j < 0:
                use1 = True
            elif nums1[i] > nums2[j]:
                use1 = True
            else:
                use1 = False

            if use1:
                nums1[cur] = nums1[i]
                i -= 1
            else:
                nums1[cur] = nums2[j]
                j -= 1



