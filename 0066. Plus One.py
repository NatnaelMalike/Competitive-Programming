class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        rem = []
        for digit in digits:
            num = (num * 10) + digit
        num += 1
        while num > 0:
           rem.append(num % 10)
           num = num // 10
        return reversed(rem)
        