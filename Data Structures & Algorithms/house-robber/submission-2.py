class Solution:
    def rob(self, nums: List[int]) -> int:
        num_houses = len(nums)
        cache = {}

        def dp(num, cache):
            if num >= num_houses:
                return 0
            if num in cache:
                return cache[num]

            money_skip_1 = dp(num + 2, cache)
            money_skip_2 = dp(num + 3, cache)

            if money_skip_1 > money_skip_2:
                cache[num] = money_skip_1 + nums[num]
                return cache[num]
            else:
                cache[num] = money_skip_2 + nums[num]
                return cache[num]
        
        return max(dp(0, cache), dp(1, cache))
        