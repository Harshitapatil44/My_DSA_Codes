# Array implementation - (done)
# Linked List implementation - (done)
# Priority queue - (done) 
# Queue Application - 
    # 1. CPU Scheduling (done) 
    # 2. Printer Queue (done) 
    # 3. BFS (Breadth First Search) (done) 
    # 4. Ticket/Waiting Line Systems (done) 
    # 5. Message/Task Scheduling (done) 

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
class priorityqueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, priority, val):
        self.items.append((priority, val))

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return

        highest = 0
        for i in range(1, len(self.items)):
            if self.items[i][0] < self.items[highest][0]:
                highest = i

        return self.items.pop(highest)[1]


pq = priorityqueue()
pq.enqueue(2, "Task 1")
pq.enqueue(1, "Task 2")
pq.enqueue(3, "Task 3")

print(pq.dequeue())  
print(pq.dequeue())  
print(pq.dequeue()) 


#Queue Applications :- 
#1. CPU Shedulling- 
class CPU_Shedulling:
    def __init__(self):
        self.items = []

    def insert(self, process, burst_time):
        self.items.append((process, burst_time))

    def delete(self):
        if len(self.items) == 0:
            print("Queue is Empty")
            return

        return self.items.pop(0)


cs = CPU_Shedulling()

cs.insert("P1", 5)
cs.insert("P2", 3)
cs.insert("P3", 6)
cs.insert("P4", 4)

waiting_time = 0
total_waititng = 0


print("Process\tBurst Time\tWaiting Time\tTurnout Time")

while len(cs.items) > 0:
    process, burst_time = cs.delete()

    Turnout_time = waiting_time + burst_time

    print(f"{process}\t{burst_time}\t\t{waiting_time}\t\t{Turnout_time}")

    total_waititng += waiting_time
    waiting_time += burst_time

avg_waititng = total_waititng / 4

print("Average Waiting Time: ", avg_waititng)


# 2. Printer Queue - 
class Printer_queue:
    def __init__(self):
        self.items = []

    def insert(self, document, pages):
        return self.items.append((document, pages))

    def delete(self):
        if len(self.items) == 0:
            print("Queue is Empty")
            return
        return self.items.pop(0)


pq = Printer_queue()

pq.insert("Resume.pdf", 1)
pq.insert("Project.pptx", 27)
pq.insert("Theausus.docs", 150)
pq.insert("Result.xlsx", 15)

print("Documents\t\tPages")

total_pages = 0

while len(pq.items) > 0:
    document, pages = pq.delete()
    print(f"{document}\t\t{pages}")
    
    total_pages += pages

print("Total Pages: ", total_pages)

# 3. BFS (Breadth First Search) 
class BFS:
    def __init__(self):
        self.items = []

    def insert(self, val):
        return self.items.append(val)

    def delete(self):
        if len(self.items) == 0:
            print("Queue is Empty")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


def print_BFS(graph, start):
    visited = set()
    q = BFS()
    visited.add(start)
    q.insert(start)

    while not q.is_empty():
        node = q.delete()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.insert(neighbor)


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}
print("BFS Traversal: ")
print_BFS(graph, "A")


# 4. Ticket/Waiting Line Systems 
class TicketQueue:
    def __init__(self):
        self.items = []

    def insert(self, Customer):
        return self.items.append(Customer)

    def delete(self):
        if len(self.items) == 0:
            print("No one at Counter...!!!")
            return None
        return self.items.pop(0)


tq = TicketQueue()

print("Ticket Queue: ")

tq.insert("Customer 1")
tq.insert("Customer 2")
tq.insert("Customer 3")
tq.insert("Customer 4")

while len(tq.items) > 0:
    customer = tq.delete()
    print(customer)























