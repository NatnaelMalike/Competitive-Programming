class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        i = 0
        current = self.head
        while current:
            if i == index:
                return current.val
            i += 1
            current = current.next
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        dummy = ListNode()
        dummy.next = self.head
        current = dummy

        for _ in range(index):
            if current.next is None:
                return  # Index is greater than length
            current = current.next

        new_node = ListNode(val)
        new_node.next = current.next
        current.next = new_node
        self.head = dummy.next  # Update head in case inserted at index 0

    def deleteAtIndex(self, index: int) -> None:
        dummy = ListNode()
        dummy.next = self.head
        current = dummy

        for _ in range(index):
            if current.next is None:
                return  # Invalid index
            current = current.next

        if current.next:
            current.next = current.next.next
        else:
            return

        self.head = dummy.next  # Update head if deleted index 0

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)