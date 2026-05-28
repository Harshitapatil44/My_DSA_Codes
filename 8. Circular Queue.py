class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.front = self.rear = -1
        self.items = [None] * size

    def enqueue(self, val):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.items[self.rear] = val
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = val

    def deque(self):
        if self.front == -1:
            print("Queue is Empty")
        elif self.front == self.rear:
            print(self.items[self.front])
            self.front = self.rear = -1
        else:
            print(self.items[self.front])
            self.front = (self.front + 1) % self.size


cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)

cq.deque()
cq.deque()
cq.deque()
cq.deque()

