class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        for _ in range(index):
            curr = curr.next

        return curr.val


    def addAtHead(self, val: int) -> None:
        new = Node(val)

        if self.size == 0:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head = new

        self.size += 1


    def addAtTail(self, val: int) -> None:
        new = Node(val)

        if self.size == 0:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.size:
            self.addAtTail(val)
            return

        new = Node(val)
        curr = self.head

        for _ in range(index - 1):
            curr = curr.next

        new.next = curr.next
        curr.next = new

        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        # Delete head
        if index == 0:
            self.head = self.head.next
            self.size -= 1

            # The list became empty
            if self.size == 0:
                self.tail = None

            return

        curr = self.head

        for _ in range(index - 1):
            curr = curr.next

        # Are we deleting the tail?
        if curr.next == self.tail:
            self.tail = curr

        curr.next = curr.next.next
        self.size -= 1