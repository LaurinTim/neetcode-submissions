class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        top_k = sorted(freq_map, key=freq_map.get, reverse=True)
        return top_k[:k]

        