class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for index in range(m - 1, -1, -1):
            nums1[index + n] = nums1[index]

        mp = n
        np = 0

        index = 0
        while np < n:
            if mp < m + n and nums1[mp] < nums2[np]:
                nums1[index] = nums1[mp]
                mp += 1
            else:
                nums1[index] = nums2[np]
                np += 1
            index += 1