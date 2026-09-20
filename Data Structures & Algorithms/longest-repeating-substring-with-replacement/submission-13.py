class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        char_dict = defaultdict(int)
        longest = 0
        max_count = 0

        for r in range(len(s)):
            char_dict[s[r]] += 1
            max_count = max(max_count, char_dict[s[r]])
            while r - l + 1 - max_count > k:
                char_dict[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
        
        return longest