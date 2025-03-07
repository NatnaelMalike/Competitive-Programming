class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        per_to_hei = {}
        for i in range(len(names)):
            per_to_hei[heights[i]] = names[i]
        sortedPer = dict(sorted(per_to_hei.items()))
        return reversed(sortedPer.values())
        