class Solution:
    def isValid(self, s: str) -> bool:
        braDict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        for b in s:
            if b in braDict:
                stack.append(b)
            else:
                if stack and b == braDict.get(stack[-1]):
                    stack.pop()
                else:
                    return False
        return not stack