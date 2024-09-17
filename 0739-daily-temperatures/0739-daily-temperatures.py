class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n
        for i,v in enumerate(temperatures):
            while stack and stack[-1][0] < v:
                stk_v, stk_i = stack.pop()
                res[stk_i] = i - stk_i
            stack.append((v, i)) 
        return res

        