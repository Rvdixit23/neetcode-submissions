class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge sort
        return self.sort(nums, 0, len(nums) - 1)

    def sort(self, nums, start, end):
        if start == end:
            return [nums[start]]
        # if isOdd(start, end):
        #     splitPoint = (start + end) // 2
        #     arr1 = self.sort(nums, start, splitPoint)
        #     arr2 = self.sort(splitPoint + 1, end)
        # elif isEven(start, end):

        splitPoint = (start + end) // 2
        arr1 = self.sort(nums, start, splitPoint)
        l1 = len(arr1)
        arr2 = self.sort(nums, splitPoint + 1, end)
        l2 = len(arr2)

        p1 = 0
        p2 = 0

        solution = []

        while p1 < l1 and p2 < l2:
            if arr1[p1] < arr2[p2]:
                solution.append(arr1[p1])
                p1 += 1
            else:
                solution.append(arr2[p2])
                p2 += 1

        if p1 == l1:
            arrayToAppend = arr2
            positionStart = p2
            positionEnd = l2 - 1
        elif p2 == l2:
            arrayToAppend = arr1
            positionStart = p1
            positionEnd = l1 - 1

        solution.extend(arrayToAppend[positionStart:positionEnd + 1])

        return solution
        

    # def isOdd(self, start, end):
    #     return end - start % 2 == 0
    
    # def isEven(self, start, end):
    #     return end - start % 2 == 1
        