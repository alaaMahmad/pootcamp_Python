class MyCircularQueue(object):

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = 0
        self.count = 0

    def enQueue(self, value):
        if self.isFull():
            return False
        
        tail = (self.head + self.count) % self.k
        self.queue[tail] = value
        self.count += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        
        self.head = (self.head + 1) % self.k
        self.count -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self):
        if self.isEmpty():
            return -1
        
        tail = (self.head + self.count - 1) % self.k
        return self.queue[tail]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.k


q = MyCircularQueue(3)

print("Enqueue Operations:")
print("Enqueue 1:", q.enQueue(1))
print("Enqueue 2:", q.enQueue(2))
print("Enqueue 3:", q.enQueue(3))
print("Enqueue 4:", q.enQueue(4))

print("\nFront and Rear Operations:")
print("Front element is:", q.Front())
print("Rear element is:", q.Rear())

print("\nDequeue Operations:")
print("Dequeued:", q.deQueue())
print("Enqueue 4:", q.enQueue(4))
print("New Rear element is:", q.Rear())

print("\nEmptying Queue:")
print("Dequeued:", q.deQueue())
print("Dequeued:", q.deQueue())
print("Dequeued:", q.deQueue())
print("Dequeued:", q.deQueue())