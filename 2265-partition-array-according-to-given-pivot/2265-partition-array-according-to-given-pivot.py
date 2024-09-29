class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        middle = [] 
        for x in nums:
            if x > pivot:
                right.append(x)
            elif x < pivot:
                left.append(x)
            else:
                middle.append(x)
        return left + middle + right
        