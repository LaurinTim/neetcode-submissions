class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [-1 * n for n in nums]
        heapq.heapify(minHeap)

        while k > 0:
            val = heapq.heappop(minHeap)
            k -= 1

        return -val
        