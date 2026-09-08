class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsl = len(nums)
        for i in range(numsl):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return [j, i]