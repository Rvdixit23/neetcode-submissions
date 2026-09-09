class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sortedIndex = 0
        for index, ele in enumerate(nums):
            moveUp = ele
            for ii in range(sortedIndex):
                if nums[ii] > moveUp:
                    nums[ii], moveUp = moveUp, nums[ii]
            nums[index] = moveUp
            sortedIndex += 1
        return nums

# [3, 2, 5, 7]
# [2, 2, 5, 7] moveup 3
# mu 2
# si 2
# ii 0
