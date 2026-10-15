class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        answer = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] == target:
                    answer.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        return  answer
            