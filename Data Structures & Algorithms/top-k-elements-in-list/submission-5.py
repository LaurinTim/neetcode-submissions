class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] += 1
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for c in range(len(nums), 0, -1):
            for n in freq[c]:
                if len(res) == k:
                    return res
                res.append(n)

        return res        