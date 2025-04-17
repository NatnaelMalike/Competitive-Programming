# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing the 2 half
        prev = None
        while slow: 
            next_temp = slow.next
            slow.next = prev
            slow.next = prev
            prev = slow
            slow = next_temp

        #compare
        first , second = head , prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True