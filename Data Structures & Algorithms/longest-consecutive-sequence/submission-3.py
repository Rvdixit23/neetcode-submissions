class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            freq = {}
            for num in nums:
                freq[num] = 1
            for num in nums:
                if freq[num] == 1:
                    isSequence = True
                    nextNum = num
                    while isSequence:
                        nextNum += 1
                        # print(num, nextNum) 2,3,4,6,8,1
                        if nextNum in freq and freq[nextNum] != -1:
                            freq[num] += freq[nextNum]
                            freq[nextNum] = -1
                        else:
                            isSequence = False
                # print(freq)
            return freq[max(freq, key = lambda x: freq[x])]
        return 0

        