class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        selfDivisible = []
        for number in range(left, right+1):
            isDivisible = True
            num = number
            remArr = []
            while(True):
                if(num >= 1 and num <= 9):
                    remArr.append(num)
                    break
                rem = num % 10
                remArr.append(rem)
                num = num // 10
            if( 0 in remArr):
                continue
            for divider in remArr:
                if(number % divider != 0):
                    isDivisible = False
                    break
            if(isDivisible):
                selfDivisible.append(number)
        return selfDivisible
