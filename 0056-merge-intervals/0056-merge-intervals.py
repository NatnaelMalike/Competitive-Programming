class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x: x[0])
        temp = intervals[0]
        for i in range(1, len(intervals)):
            if temp[1] >= intervals[i][0]:
                temp[1] = max(temp[1],intervals[i][1])
            else:
                ans.append(temp)
                temp = intervals[i]
        ans.append(temp)
        return ans