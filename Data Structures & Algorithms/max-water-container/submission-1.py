class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        maxArea = 0
        while start < end:
            maxArea = max((end - start) * min(heights[start], heights[end]), maxArea)
            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1
        return maxArea
