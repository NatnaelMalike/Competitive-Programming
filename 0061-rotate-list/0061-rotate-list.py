# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        l = 1
        tail = head
        while tail.next:
            tail = tail.next
            l += 1
        k = k % l
        if k == 0:
            return head
        a = l - k
        last = head
        for _ in range(1,a):
            last = last.next
        newHead = last.next
        last.next = None
        tail.next = head
        return newHead
        
        




