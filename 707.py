class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None # 可以單純當成C++的pointer var，just store address
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        cur = self.head
        
        for _ in range(index):
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:
        self.insertNode(0, val)

    def addAtTail(self, val: int) -> None:
        self.insertNode(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        self.insertNode(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size:
            return
        
        cur = self.head

        if index==0:
            self.head = cur.next
            del cur
        else:
            for _ in range(index-1):
                cur = cur.next
            temp = cur.next
            cur.next = temp.next
            del temp

        self.size -= 1

    def insertNode(self, index: int, val: int) -> None:
        if index<0 or index>self.size:
            return
        
        cur = self.head
        newNode = ListNode(val)
        
        if index==0:
            newNode.next = self.head
            self.head = newNode
        else:
            for _ in range(index-1): # 我要前一格才能insert
                cur = cur.next
            newNode.next = cur.next
            cur.next = newNode

        self.size += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
