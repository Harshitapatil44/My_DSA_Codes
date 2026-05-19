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
            while t1.next is not self.head:
                t1 = t1.next
            t1.next = temp
            temp.next = self.head
        else:
            self.head = temp
            temp.next = temp

    def insertAtBeginning(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            temp.next = temp
        else:
            t1 = self.head
            while t1.next is not self.head:
                t1 = t1.next

            temp.next = self.head
            t1.next = temp
            self.head = temp

    def insertAtMid(self, value, x):
        temp = Node(value)

        # If list is empty
        if self.head is None:
            return

        t1 = self.head

        # Special case: if head itself is x
        if self.head.data == x:
            temp.next = self.head.next
            self.head.next = temp
            return

        # Traverse until we come back to head
        while t1.next is not self.head:
            if t1.data == x:
                temp.next = t1.next
                t1.next = temp
                break
            t1 = t1.next

    def deleteNode(self, value):
        # Case 1: Empty list
        if self.head is None:
            return

        # Case 2: Only one node
        if self.head.next == self.head:
            if self.head.data == value:
                self.head = None
            return

        t1 = self.head
        prev = None

        # Case 3: Deleting head
        if self.head.data == value:

            # Find last node
            while t1.next is not self.head:
                t1 = t1.next

            t1.next = self.head.next
            self.head = self.head.next
            return

        # Case 4 & 5: Middle or Last node
        prev = self.head
        t1 = self.head.next

        while t1 is not self.head:
            if t1.data == value:
                prev.next = t1.next
                break
            prev = t1
            t1 = t1.next

    def printLL(self):
        t1 = self.head
        while t1.next is not self.head:
            print(t1.data)
            t1 = t1.next
        print(t1.data)


obj = SinglyLinkedList()
obj.insertAtBeginning(5)
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtMid(40, 20)
obj.deleteNode(20)
obj.printLL()
