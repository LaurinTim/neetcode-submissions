class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        max_nums = list()
        curr_max = max(nums[l:r + 1])
        max_nums.append(curr_max)

        while r < len(nums) - 1:
            l += 1
            r += 1

            if nums[r] >= curr_max:
                curr_max = nums[r]
            elif nums[l - 1] == curr_max:
                curr_max = max(nums[l:r + 1])
            
            max_nums.append(curr_max)
        
        return max_nums    
        