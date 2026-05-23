class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def insertAtEnd(self, val):
        self.items.append(val)

    def insertAtFront(self, val):
        self.items.insert(0, val)

    def deleteAtFront(self):
        if self.isEmpty():
            print("Deque is Empty")
        return self.items.pop(0)

    def deleteAtEnd(self):
        if self.isEmpty():
            print("Deque is Empty")
        return self.items.pop()


dq = Deque()
dq.insertAtEnd(10)
dq.insertAtFront(20)
dq.insertAtEnd(30)
dq.insertAtEnd(40)
dq.insertAtFront(50)

print(dq.deleteAtEnd())
print(dq.deleteAtEnd())
print(dq.deleteAtFront())
print(dq.deleteAtFront())
print(dq.deleteAtEnd())
dq.deleteAtFront()
