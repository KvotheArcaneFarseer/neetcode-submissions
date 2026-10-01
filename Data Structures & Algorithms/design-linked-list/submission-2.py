class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        curr = self.head
        if index < 0 or index >= self.size:
            return -1
        else:
            for ooo in range(index):
                curr = curr.next
            return curr.val


    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head
        self.head = new
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        last = Node(val)
        index = self.head
        if self.size == 0:
            self.head = last
            last.next = None
        else:
            while index.next is not None:
                index = index.next
            index.next = last
        self.size += 1
        
    
    def addAtIndex(self, index: int, val: int) -> None:
        insertval = Node(val)
        entry = self.head
        secondentry = self.head
        if index > self.size:
            exit
        else:
            for i in range(index-1):
                entry = entry.next
            insertval.next = entry.next
            entry.next = insertval
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        entry = self.head
        if self.size == 0:
            exit
        elif index >= self.size or index < 0:
            exit
        elif index == 0:
            self.head = entry.next
            self.size -= 1
        else:
            for i in range(index-1):
                entry = entry.next
            entry.next = entry.next.next
            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)