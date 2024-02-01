class Solution:
    def findLucky(self, arr: List[int]) -> int:
            dict = {}
            lucky = -1
            for ele in arr:
                if ele in dict:
                    dict[ele] += 1
                else:
                    dict[ele] = 1
            for key in dict:
                if key == dict[key]:
                    lucky = max(lucky,key)
            return lucky