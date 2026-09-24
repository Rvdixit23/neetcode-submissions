class MinStack:

    def __init__(self):
        [0, 1, 2]
        [0]
        self.stack = deque()
        self.minStack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            if val <= self.minStack[-1]:
                self.minStack.append(val)
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.minStack[-1] == val:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
