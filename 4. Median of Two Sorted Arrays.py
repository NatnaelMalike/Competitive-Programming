class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        wholeArr = nums1 + nums2
        wholeArr.sort()
        n = len(wholeArr)
        if(n % 2 == 0):
            middle = floor(n / 2)
            return (wholeArr[middle-1] + wholeArr[middle])/ 2;
        else:
            middle = floor((n + 1) / 2) 
            return (wholeArr[middle-1])
