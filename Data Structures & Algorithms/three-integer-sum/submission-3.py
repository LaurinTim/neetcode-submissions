class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        base = 0
        res = []
        sorted_nums = sorted(nums)
        while base < len(nums) - 2:
            l, r = base + 1, len(nums) - 1
            if base > 0 and sorted_nums[base] == sorted_nums[base - 1]:
                base += 1
                continue
            while l < r:
                s = sorted_nums[base] + sorted_nums[l] + sorted_nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    curr_res = [sorted_nums[base], sorted_nums[l], sorted_nums[r]]
                    if not curr_res in res:
                        res.append(curr_res)
                    l += 1
            base += 1
        return res


        