class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = deque()
        for index, t in enumerate(temperatures):
            while len(stack) > 0 and t > stack[-1][1]:
                cindex, cval = stack.pop()
                answer[cindex] = index - cindex
            stack.append((index, t))
        return answer


