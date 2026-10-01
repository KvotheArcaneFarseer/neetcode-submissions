class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        current = self.head
        for i in range(index):
            if current is None:
                return -1
            current = current.next
        if current is None:
            return -1
        return current.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        current = self.head
        if self.head is None:
            self.head = new_node
        else:
            while current.next != None:
                current = current.next
            current.next = new_node

    def remove(self, index: int) -> bool:
        current = self.head
        if self.head is None:
            return False
        if index == 0:
            self.head = current.next
            return True
        if index < 0:
            return False
        for i in range(index-1):
            if current is None:
                return False
            elif current.next is None:
                return False
            else:
                current = current.next
        if current.next is None:
            return False
        else:
            current.next = current.next.next
            return True

    def getValues(self) -> List[int]:
        haha = []
        current = self.head
        while current != None:
            haha.append(current.val)
            current = current.next
        return haha
        
