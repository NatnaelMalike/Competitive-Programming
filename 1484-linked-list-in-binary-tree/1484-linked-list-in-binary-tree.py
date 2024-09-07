# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head, root):
        return self.dfs(head, head, root)

    def dfs(self, head, curr, root):
        if curr is None:  
            return True
        if root is None:  
            return False
        
        if curr.val == root.val:
            curr = curr.next  
        elif head.val == root.val:
            head = head.next 
        else:
            curr = head 

       
        return self.dfs(head, curr, root.left) or self.dfs(head, curr, root.right)
        