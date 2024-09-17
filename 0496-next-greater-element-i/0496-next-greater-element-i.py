class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            j = nums2.index(i)
            ptr = j + 1
            while(ptr < len(nums2)):
                if nums2[j] < nums2[ptr]:
                    res.append(nums2[ptr])
                    break
                ptr += 1
            if ptr >= len(nums2):
                res.append(-1)
        return res
            