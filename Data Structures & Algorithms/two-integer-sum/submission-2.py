class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsl = len(nums)
        
        subdict = {}

        for index in range(numsl):
            subdict[target - nums[index]] = index

        for index in range(numsl):
            if subdict.get(nums[index], None) and index != subdict[nums[index]]:
                return [index, subdict[nums[index]]]
        
        
        # for i in range(numsl):
        #     for j in range(i):
        #         if nums[i] + nums[j] == target:
        #             return [j, i]

