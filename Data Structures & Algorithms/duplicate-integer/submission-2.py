class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains = set()
        for val in nums:
            if val in contains:
                return True
            contains.add(val)
        return False
        