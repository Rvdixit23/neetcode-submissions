class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for ele in nums:
            count[ele] += 1

        cp = 0
        index = 0
        while index < len(nums):
            if count[cp] > 0:
                nums[index] = cp
                index += 1
                count[cp] -= 1
            else:
                cp += 1

        