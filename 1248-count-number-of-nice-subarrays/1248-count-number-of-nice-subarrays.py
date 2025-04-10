class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        odd_count = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1 

        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            
            count += prefix_counts[odd_count - k]
            prefix_counts[odd_count] += 1

        return count

        