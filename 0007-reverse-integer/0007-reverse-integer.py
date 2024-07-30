class Solution:
    def reverse(self, x: int) -> int:
        reverse=0
        if x<0:
            x=x*-1
            while(x!=0):
                last=x%10
                reverse=(reverse*10)+last
                x=x//10
            if reverse < -2147483648 or reverse > 2147483647:
                return 0
            return reverse*-1
        else:
             while(x!=0):
                last=x%10
                reverse=(reverse*10)+last
                x=x//10
             if reverse < -2147483648 or reverse > 2147483647:
                return 0
             return reverse



            