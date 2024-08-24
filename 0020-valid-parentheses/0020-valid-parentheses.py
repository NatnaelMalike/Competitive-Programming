class Solution:
    def isValid(self, s: str) -> bool:
        dc={'(':')','{':'}','[':']'}
        stack=[]
        for x in s:
            if x in dc:
                stack.append(x)
            elif len(stack)==0 or dc[stack.pop()]!=x:
                return False
        return len(stack)==0