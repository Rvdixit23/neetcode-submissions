class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mp = m - 1
        np = n - 1

        index = m + n - 1
        while np > -1:
            if mp > -1 and nums1[mp] > nums2[np]:
                nums1[index] = nums1[mp]
                mp -= 1
            else:
                nums1[index] = nums2[np]
                np -= 1
            index -= 1