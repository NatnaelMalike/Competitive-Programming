class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic_s = Counter(s)
        dic_t = Counter(t)
        steps = 0
        
        for key, value in dic_s.items():
            if key in dic_t:
                if value > dic_t[key]:
                    steps += value - dic_t[key]
            else:
                steps += value
                
        return steps

