class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        maj = len(nums)/2
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
            if freq[i] >= maj:
                return i