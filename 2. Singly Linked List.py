class Node:
    def __init__(self, data, Next=None):
        self.data = data
        self.next = Next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head is not None:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insertAtBeginning(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertAtMid(self, value, x):
        temp = Node(value)
        if self.head is not None:
            t1 = self.head
            if self.head.data == x:
                temp.next = self.head
                self.head = temp
            while t1.next is not None:
                if t1.data == x:
                    temp.next = t1.next
                    t1.next = temp
                    break
                else:
                    t1 = t1.next
            if self.head is not None:
                t1 = self.head
                while t1.next is not None:
                    t1 = t1.next
                t1.next = temp

    def deleteLL(self, value):
        if self.head.data == value:
            self.head = self.head.next
        else:
            t1 = self.head
            prev = t1
            while t1.next is not None:
                if t1.data == value:
                    prev.next = t1.next
                    break
                else:
                    prev = t1
                    t1 = t1.next

    def printLL(self):
        t1 = self.head
        while t1.next is not None:
            print(t1.data)
            t1 = t1.next
        print(t1.data)


obj = SinglyLinkedList()
obj.insertAtBeginning(5)
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtMid(40, 30)
obj.deleteLL(20)
obj.printLL()
