class Solution:
    def isValid(self, s: str) -> bool:
        dicPair = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        if s[0] not in dicPair:
            return False
        stack = []
        for bra in s:
            if stack and dicPair[stack[-1]] == bra:
                stack.pop()
            elif bra in dicPair:
                stack.append(bra)
            else:
                return False
        return len(stack) == 0
        