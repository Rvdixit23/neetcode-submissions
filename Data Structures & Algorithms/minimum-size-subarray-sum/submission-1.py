class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        if sum(nums) < target:
            return 0

        best = len(nums)
        total = nums[0]
        while r < len(nums):
            # print(nums[l:r + 1])
            if total < target and r - l + 1 < best:
                r += 1
                if r == len(nums):
                    return best
                total += nums[r]
            else:
                best = min(best, r - l  + 1)
                total -= nums[l]
                l += 1
            # print("Best :", best)

        return best
            
        