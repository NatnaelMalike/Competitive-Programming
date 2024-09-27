class Solution:
    @staticmethod
    def doBackSpace(s):
            stack = []
            for i in s:
                if i != '#':
                    stack.append(i)
                elif stack:
                    stack.pop()
            return stack
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        return self.doBackSpace(s) == self.doBackSpace(t)
