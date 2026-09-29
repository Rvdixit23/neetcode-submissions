
class FreqStack:

    def __init__(self):
        self.fkd = {}
        self.fkd[0] = set()
        self.nkd = {}
        self.maxFreq = 0
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.nkd[val] = self.nkd.get(val, 0) + 1
        if self.nkd[val] not in self.fkd:
            self.fkd[self.nkd[val]] = set()
        self.fkd[self.nkd[val]].add(val)
        
        if val in self.fkd[self.nkd[val] - 1]:
            self.fkd[self.nkd[val] - 1].remove(val)
        self.maxFreq = max(self.maxFreq, self.nkd[val])

    def pop(self) -> int:
        poppedStack = []
        poppedEle = None
        while self.stack and poppedEle not in self.fkd[self.maxFreq]:
            poppedStack.append(poppedEle)
            poppedEle = self.stack.pop()
        
        # Update fkd and nkd
        self.nkd[poppedEle] -= 1
        self.fkd[self.maxFreq].remove(poppedEle)
        self.fkd[self.maxFreq - 1].add(poppedEle)

        if not self.fkd[self.maxFreq]:
            self.maxFreq -= 1

        # Put poppedStack back in reverse
        while poppedStack:
            self.stack.append(poppedStack.pop())
        
        return poppedEle


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()