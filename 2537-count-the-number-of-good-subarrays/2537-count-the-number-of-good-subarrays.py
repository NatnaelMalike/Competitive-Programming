class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
            n = len(nums)
            left = 0
            pair_count = 0
            freq = defaultdict(int)
            result = 0

            for right in range(n):
                pair_count += freq[nums[right]]
                freq[nums[right]] += 1

                while pair_count >= k:
                    result += n - right 
                    freq[nums[left]] -= 1
                    pair_count -= freq[nums[left]]
                    left += 1

            return result