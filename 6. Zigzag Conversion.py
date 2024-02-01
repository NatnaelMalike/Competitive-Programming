class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
        beg = 0
        last = 0
        zigZag = [[]for _ in range(numRows)]
        output = []
        for l in s:
            if(beg < numRows):
                zigZag[beg].append(l)
                beg += 1
                if(beg == numRows):
                    last = beg -2
            elif(last >= 0):
                zigZag[last].append(l)
                last -= 1
                if(last == -1):
                    beg = 1
        for i in range(numRows):
            output.append(''.join(zigZag[i]))
        return ''.join(output)
        
