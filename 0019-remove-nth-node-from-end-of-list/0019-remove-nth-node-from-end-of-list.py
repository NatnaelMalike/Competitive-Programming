# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        temp=head
        while(temp!=None):
            count+=1
            temp=temp.next
        if count==n:
            return head.next
        pose=count-n
        temp=head
        i=0
        temp2=temp
        while(i!=pose):
            i+=1
            temp2=temp
            temp=temp.next
        
        temp2.next=temp.next
        temp.next=None
        return head

