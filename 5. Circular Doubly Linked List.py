class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next


class CircularDoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            temp.next = self.head
            temp.prev = self.head
        else:
            t1 = self.head
            while t1.next != self.head:
                t1 = t1.next
            t1.next = temp
            temp.prev = t1
            temp.next = self.head
            self.head.prev = temp

    def insertAtBeg(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            temp.next = temp
            temp.prev = temp
        else:
            last = self.head.prev

            temp.next = self.head
            temp.prev = last

            last.next = temp
            self.head.prev = temp

            self.head = temp

    def insertatmid(self, value, x):
        temp = Node(value)
        if self.head is None:
            print("Linked list is Empty")
        else:
            t1 = self.head
            while t1.next != self.head:
                if t1.data == x:
                    temp.next = t1.next
                    temp.prev = t1
                    t1.next.prev = temp
                    t1.next = temp
                    return
                t1 = t1.next
            if t1.data == x:
                temp.next = t1.next
                temp.prev = t1
                t1.next.prev = temp
                t1.next = temp
                return

    def deleteCLL(self, value):
        if self.head is None:
            print("Linked list is Empty")
        else:
            t1 = self.head
            while t1.next != self.head:
                if t1.data == value:
                    t1.prev.data = t1.data
                    t1.prev.next = t1.next
                    t1.next.prev = t1.prev
                    return
                t1 = t1.next
            if t1.data == value:
                t1.prev.data = t1.data
                t1.prev.next = t1.next
                t1.next.prev = t1.prev
                return

    def printCDLL(self):
        t1 = self.head
        while t1.next != self.head:
            print(t1.data, end=" ")
            t1 = t1.next
        print(t1.data)


obj = CircularDoublyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(5)
obj.insertatmid(15, 10)
obj.deleteCLL(20)
obj.printCDLL()
