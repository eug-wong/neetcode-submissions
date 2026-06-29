class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = []
        self.items = 0

    def enQueue(self, value: int) -> bool:
        if self.items < self.capacity:
            self.queue.append(value)
            self.items += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.items > 0:
            self.queue = self.queue[1: ]
            self.items -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        if self.items > 0:
            return self.queue[0]
        else:
            return -1

    def Rear(self) -> int:
        if self.items > 0:
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.items == 0

    def isFull(self) -> bool:
        return self.items == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()