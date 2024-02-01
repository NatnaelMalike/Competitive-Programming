class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        for i,ele in enumerate(nums):
            if ele in dict:
                if abs(dict[ele]-i) <= k:
                    return True
                else:
                    dict[ele] = i
            else:
                dict[ele] = i
        return False