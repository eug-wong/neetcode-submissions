class MyHashMap:

    def __init__(self):
        self.arr = []

    def put(self, key: int, value: int) -> None:
        for n in self.arr:
            if n[0] == key:
                n.append(value)
                return

        self.arr.append([key, value])

    def get(self, key: int) -> int:
        for n in self.arr:
            if n[0] == key:
                return n[-1]
        
        return -1

        

    def remove(self, key: int) -> None:
        for n in self.arr:
            if n[0] == key:
                self.arr.remove(n)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)