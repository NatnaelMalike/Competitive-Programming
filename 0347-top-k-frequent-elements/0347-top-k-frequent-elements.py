class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        res = []
        for num in nums:
            if num in freqDict:
                freqDict[num] += 1
            else:
                freqDict[num] = 1
        ans = sorted(freqDict.values(), reverse = True)
        ans = ans[0:k]
        for key, value in freqDict.items():
            if value in ans:
                res.append(key)
        return res


        