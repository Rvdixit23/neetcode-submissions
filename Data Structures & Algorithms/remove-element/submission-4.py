class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        currentEnd = len(nums) - 1
        index = 0
        while (index <= currentEnd):
            if nums[index] == val:
                nums[index] = nums[currentEnd]
                currentEnd -= 1
            else:
                index += 1
        return index