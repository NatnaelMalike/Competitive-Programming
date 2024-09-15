
class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'(':')','{':'}','[':']'}
        stack = []
        for x in s:
            if x in pair:
                stack.append(x)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if pair[popped] != x:
                        return False
        return not stack

    
    
         


       
       