class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [-1 * n for n in nums]
        heapq.heapify(minHeap)

        for _ in range(k):
            val = heapq.heappop(minHeap)

        return -val
        