class Solution:
    def addDigits(self, num: int) -> int:
        # while num >= 10:
        #     num = sum(int(digit) for digit in str(num))
        # return num
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        return num % 9