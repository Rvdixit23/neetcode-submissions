class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        workIndex = 0
        seeIndex = 1
        for seeIndex in range(1, len(nums)):
            if nums[seeIndex] != nums[workIndex]:
                workIndex += 1
                nums[workIndex] = nums[seeIndex]
        return workIndex + 1