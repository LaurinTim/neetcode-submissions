class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        k = n - 1
        index = m + n - 1
        while i >= 0 and k >= 0:
            if nums1[i] > nums2[k]:
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[k]
                k -= 1
            index -= 1
        
        if i < 0 and k >= 0:
            nums1[:index + 1] = nums2[:k + 1]
