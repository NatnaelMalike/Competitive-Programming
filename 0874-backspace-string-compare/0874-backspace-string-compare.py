class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for i in s:
            if i != '#':
                stack.append(i)
            elif stack:
                stack.pop()
        res1 = [x for x in stack]
        stack = []
        for i in t:
            if i != '#':
                stack.append(i)
            elif stack:
                stack.pop()
        return ''.join(res1) == ''.join(stack)


        