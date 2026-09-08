class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsl = len(nums)
        
        subdict = {}

        for index in range(numsl):
            if subdict.get(nums[index], -1) > -1:
                return [subdict[nums[index]], index]
            subdict[target - nums[index]] = index