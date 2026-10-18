class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]

        start, stop = 0, len(nums) - 1

        while start != stop:
            pos = start + (stop - start) // 2
            val = nums[pos]
            if val > nums[stop]:
                start = pos + 1
            else:
                stop = pos
        
        return nums[start]
