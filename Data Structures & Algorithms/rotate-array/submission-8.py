class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, start, end):
        for i in range((end - start)//2 + 1):
            temp = nums[start + i]
            nums[start + i] = nums[end - i]
            nums[end - i] = temp

# 7 6 5 4 3 2 1

# 5 6 7 4 3 2 1

# 5 6 7 1 2 3 4
        

            