from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0

        ans = []
        self.sw = SortedList(nums[0:k])
        r = k - 1
        while r < len(nums) - 1:
            # print(self.sw)
            ans.append(self.sw[-1])
            r += 1
            self.sortSlide(toAdd=nums[r], toRem=nums[l])
            l += 1
        ans.append(self.sw[-1])
        return ans
            


    def sortSlide(self, toAdd, toRem):
        # print("removing", toRem, "adding", toAdd)
        self.sw.add(toAdd)
        self.sw.remove(toRem)


