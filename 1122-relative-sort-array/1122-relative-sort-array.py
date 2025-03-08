class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {num: idx for idx, num in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (dic.get(x, len(arr2)), x))

        