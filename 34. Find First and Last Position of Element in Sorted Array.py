class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        list1=[]
        count=0
        if target not in nums:
            return[-1,-1]
        else:
            for x in nums:
                count+=1
                if x == target:
                    list1.append(count-1)
        if len(list1)==1:
            list1.append(list1[0])
            return list1
        else:
            a=list1[len(list1)-1]
            b=list1[0]
            
        
        return [b,a]
            