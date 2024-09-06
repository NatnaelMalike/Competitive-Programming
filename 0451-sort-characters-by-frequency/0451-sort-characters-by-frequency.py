class Solution:
    def frequencySort(self, s: str) -> str:
        res = []
        dic = Counter(s)
        sorted_dic = sorted(dic.items(), key = lambda item: item[1], reverse= True)
        for ele in sorted_dic:
            res.append(ele[0]*ele[1])
        return "".join(res)

        