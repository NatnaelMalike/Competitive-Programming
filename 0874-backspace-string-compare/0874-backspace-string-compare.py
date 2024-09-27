class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def doBackSpace(s):
            stack = []
            for i in s:
                if i != "#":
                    stack.append(i)
                elif stack:
                    stack.pop()
            return stack

        return doBackSpace(s) == doBackSpace(t)
