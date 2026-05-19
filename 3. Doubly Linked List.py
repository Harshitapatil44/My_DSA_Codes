class Node:
    def __init__(self, data, Next=None, Prev=None):
        self.data = data
        self.next = Next
        self.prev = Prev


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return
        t1 = self.head
        while t1.next is not None:
            t1 = t1.next
        t1.next = temp
        temp.prev = t1

    def insertAtbeg(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insertAtMid(self, value, x):
        temp = Node(value)
        t1 = self.head

        while t1.next is not None:
            if t1.data is x:
                break
            else:
                t1 = t1.next
        temp.next = t1.next
        t1.next.prev = temp
        t1.next = temp
        temp.prev = t1

    def deleteLL(self, value):
        if self.head is None:
            print("Linked List is empty")
            return
        t1 = self.head
        if t1.data == value:
            self.head = t1.next
            self.head.prev = None
            return
        while t1.next is not None:
            if t1.data == value:
                t1.prev.next = t1.next
                t1.next.prev = t1.prev
                return
            else:
                t1 = t1.next
        if t1.data == value:
            t1.prev.next = None

    def printLL(self):
        t1 = self.head
        while t1.next is not None:
            print(t1.data, end=" <--> ")
            t1 = t1.next
        print(t1.data)


obj = DoublyLinkedList()
obj.insertAtbeg(5)
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtMid(50, 30)
obj.deleteLL(20)
obj.printLL()
