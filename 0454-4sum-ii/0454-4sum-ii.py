class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        res_dict = {}
        for n1 in nums1:
            for n2 in nums2:
                if n1+n2 in res_dict:
                    res_dict[n1+n2] += 1
                else:
                    res_dict[n1+n2] = 1

        for n3 in nums3:
            for n4 in nums4:
                if 0 - (n3+n4) in res_dict:
                    count += res_dict[0 - (n3+n4)]
        return count