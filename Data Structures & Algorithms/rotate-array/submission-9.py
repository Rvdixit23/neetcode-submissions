from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        tmp = deque(nums)

        for i in range(k):
            el = tmp.pop()
            tmp.appendleft(el)

        nums[:] = list(tmp)