class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = set(nums1)
        num2 = set(nums2)
        inter = []
        for ele  in num1:
            if ele in num2:
                inter.append(ele)
        return inter
