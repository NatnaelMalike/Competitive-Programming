class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        leng=len(nums)
        k=0
        ind=0
        comp=leng-1
        while(nums[ind]!='_'):
            if nums[ind]==val:
                nums[ind]='_'
                temp=nums[ind]
                nums[ind]=nums[comp]
                nums[comp]=temp
                comp-=1
                k+=1
            else:
                ind+=1
        return leng-k

        