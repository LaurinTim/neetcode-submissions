class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, stop = 0, len(nums) - 1

        while start != stop:
            pos = start + (stop - start) // 2
            val = nums[pos]

            if val < nums[stop]:
                if val < target <= nums[stop]:
                    start = pos + 1
                else:
                    stop = pos
            else:
                if target > val or target <= nums[stop]:
                    start = pos + 1
                else:
                    stop = pos
            
        return start if nums[start] == target else -1
        