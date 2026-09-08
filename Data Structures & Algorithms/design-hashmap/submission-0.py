class MyHashMap:

    def __init__(self):
        self.elements = []

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            self.elements.append([key, value])
        else:
            for index, ele in enumerate(self.elements):
                if ele[0] == key:
                    ele[1] = value
        

    def get(self, key: int) -> int:
        for ele in self.elements:
            if ele[0] == key:
                return ele[1]
        return -1

    def remove(self, key: int) -> None:
        if self.get(key) != -1:
            for index, ele in enumerate(self.elements):
                if ele[0] == key:
                    self.elements.pop(index)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)