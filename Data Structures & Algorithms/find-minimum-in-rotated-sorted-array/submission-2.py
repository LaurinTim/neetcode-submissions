class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, stop = 0, len(nums) - 1

        while start != stop:
            pos = start + (stop - start) // 2
            val = nums[pos]
            if val > nums[stop]:
                start = pos + 1
            else:
                stop = pos
        
        return nums[start]
