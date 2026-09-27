class Solution:
    def simplifyPath(self, path: str) -> str:
        items = path.split("/")
        stack = deque()

        stack.append("/")

        for item in items:
            if item:
                if item == ".":
                    pass
                elif item == "..":
                    if len(stack) > 1:
                        stack.pop()
                        if len(stack) > 1 and stack[-1] == "/":
                            stack.pop()
                else:
                    if stack[-1] != "/":
                        stack.append("/")
                    stack.append(item)
        return "".join(stack)
