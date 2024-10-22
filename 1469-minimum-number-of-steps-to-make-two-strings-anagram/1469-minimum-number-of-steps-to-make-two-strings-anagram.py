class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic_s = Counter(s)
        dic_t = Counter(t)
        steps = 0
        for key,value in dic_s.items():
            if key in dic_t and value > dic_t[key]:
                steps += value - dic_t[key]
            elif(key not in dic_t):
                steps += value
        return steps

