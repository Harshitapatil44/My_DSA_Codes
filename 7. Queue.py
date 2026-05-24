# Array implementation - (done)
# Linked List implementation - (done)
# Priority queue - (done) 
# Queue Application -

class Queue:
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
print(q.delete())


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


arr = Arr_queue(5)

items = list(map(int, input().split()))
for el in items:
    arr.insert(el)

while arr.front != -1:
    print(arr.delete())

# Linked List implementation:-
class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def insert(self, val):
        temp = node(val)

        if self.is_empty():
            self.front = temp
            self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp

    def delete(self):
        if self.is_empty():
            print("Queue is Empty")
            return

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return temp.data


qLL = QueueLL()
items = list(map(int, input().split()))

for el in items:
    qLL.insert(el)

while not qLL.is_empty():
    print(qLL.delete())

# Priority Queue:-
class priorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, priority, val):
        self.items.append((priority, val))

    def delete(self):
        if self.is_empty():
            print("Priority Queue is Empty")
            return

        highest = 0

        for i in range(1, len(self.items)):
            if self.items[i][0] < self.items[highest][0]:
                highest = i

        return self.items.pop(highest)[1]


pLL = priorityQueue()
pLL.insert(2, "B")
pLL.insert(1, "A")
pLL.insert(3, "C")

print(pLL.delete())
print(pLL.delete())
print(pLL.delete())







