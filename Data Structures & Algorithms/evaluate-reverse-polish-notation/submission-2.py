class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if token not in "+-*/":
                stack.append(token)
            else:
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                if token == "+":
                    result = op2 + op1
                elif token == "-":
                    result = op2 - op1
                elif token == "*":
                    result = op2 * op1
                elif token == "/":
                    result = int(op2 / op1)
                stack.append(result)
        return int(stack.pop())