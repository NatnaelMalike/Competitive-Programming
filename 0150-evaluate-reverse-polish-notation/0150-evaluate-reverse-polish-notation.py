class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oprts = ['+', '-', '/', '*']
        stack = []
        for token in tokens:
            if token not in oprts:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    res = num1 + num2
                elif token == '-':
                    res = num1 - num2
                elif token == '*':
                    res = num1 * num2
                else:
                    res = int(num1 / num2)
                stack.append(res)
        return stack[0]



        