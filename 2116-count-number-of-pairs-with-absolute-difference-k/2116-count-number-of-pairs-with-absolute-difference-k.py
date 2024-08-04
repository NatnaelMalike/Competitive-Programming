class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        num_count={}
        count = 0
        for num in nums:
            if (num-k) in num_count:
                count += num_count[num-k]
            if (num+k) in num_count:
                count += num_count[num+k]

            if num in num_count:
                num_count[num] += 1    
            else:
                num_count[num] = 1
        return count
        
        