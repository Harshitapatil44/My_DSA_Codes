# Array implementation - (done)
# Linked List implementation - (done)
# Circular queue -
# Priority queue -
# Queue Application -

"""class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def insert(self, val):
        self.items.append(val)

    def delete(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        return self.items.pop(0)


q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
q.insert(40)
q.insert(50)


print(q.delete())
print(q.delete())
print(q.delete())
print(q.delete())"""


# Array implementation:-
class Arr_queue:
    def __init__(self, size):
        self.Arr_queue = [None] * size
        self.front = -1
        self.rear = -1
        self.size = size

    def insert(self, val):
        if self.rear == self.size - 1:
            print("Queue is Full")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.Arr_queue[self.rear] = val

    def delete(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        val = self.Arr_queue[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1

        self.front += 1

        return val


q = Arr_queue(10)

items = list(map(int, input().split()))

for i in items:
    q.insert(i)

print(q.delete())
print(q.delete())
print(q.delete())

# Linked List implementation:-
