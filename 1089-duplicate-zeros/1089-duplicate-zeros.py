class Solution:
    def duplicateZeros(self, arr):
        ans = []
        for i in range(len(arr)):
            if arr[i] == 0:
                ans.append(0)
                ans.append(0)
                i += 1
            else:
                ans.append(arr[i])
        for i in range(len(arr)):
            arr[i] = ans[i]
        
        