class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        answer = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = n - 1
                print(i, j, k, l)
                while k < l:
                    s4 = nums[i] + nums[j] + nums[k] + nums[l]
                    if s4 > target:
                        l -= 1
                    elif s4 < target:
                        k += 1
                    else:
                        answer.append([nums[i], nums[j], nums[k], nums[l]])
                        l -= 1
                        k += 1
                        while nums[k] == nums[k - 1] and k < l:
                            k += 1
        return answer