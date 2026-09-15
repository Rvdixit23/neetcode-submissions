class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forPro = []
        mp = 1
        for num in nums:
            mp *= num
            forPro.append(mp)

        bacPro = [0] * len(nums)
        mp = 1
        for index in range(len(nums) - 1, -1, -1):
            mp *= nums[index]
            bacPro[index] = mp
        
        answer = [1] * len(nums)

        for index in range(len(nums)):
            toMul1 = 1
            toMul2 = 1
            if index > 0:
                toMul1 = forPro[index - 1]
            if index < len(nums) - 1:
                toMul2 = bacPro[index + 1]
            answer[index] = toMul1 * toMul2
        return answer
            