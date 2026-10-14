class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        workIndex = 0
        seeIndex = 1
        while seeIndex < len(nums):
            if nums[seeIndex] == nums[workIndex]:
                seeIndex += 1
            else:
                workIndex += 1
                nums[workIndex] = nums[seeIndex]
                seeIndex += 1
        return workIndex + 1