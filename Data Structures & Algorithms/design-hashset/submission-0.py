class MyHashSet:

    def __init__(self):
        self.elements = []
        self.length = 0
        
    def add(self, key: int) -> None:
        if not self.contains(key):
            self.elements.append(key)
        self.length += 1

    def remove(self, key: int) -> None:
        index = self.containsIndex(key)
        if index > -1:
            self.elements.pop(index)
        self.length -= 1


    def contains(self, key: int) -> bool:
        for index, ele in enumerate(self.elements):
            if ele == key:
                return True
        return False

    def containsIndex(self, key: int) -> bool:
        for index, ele in enumerate(self.elements):
            if ele == key:
                return index
        return -1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)