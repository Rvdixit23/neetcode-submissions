class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = 0

        rfzVal = -len(nums) - 2
        for i in range(len(nums)):
            # If an element in the future has been marked negative
            # It won't be considered here without abs
            val = abs(nums[i])
            if val != 0 and val <= len(nums):
                if nums[val - 1] == 0:
                    nums[val - 1] = rfzVal
                else:
                    # Don't repeat multiple numbers, hence abs
                    nums[val - 1] = -1 * abs(nums[val - 1])
        
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        
        return len(nums) + 1
                    