class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = {}
        i = 0
        for ind, val in enumerate(fruits):
            dic[val] = dic.get(val, 0) + 1
            if len(dic) > 2:
                dic[fruits[i]] -= 1
                if dic[fruits[i]] == 0: del dic[fruits[i]]
                i += 1
        return ind - i + 1
        