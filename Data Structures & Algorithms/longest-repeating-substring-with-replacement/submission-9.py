class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        char_dict = defaultdict(int)
        longest = 0

        while r < len(s):
            char_dict[s[r]] += 1
            max_char = max(char_dict, key=char_dict.get)
            replace_count = sum([bal for val,bal in char_dict.items() if val != max_char])
            while replace_count > k and l <= r:
                char_dict[s[l]] -= 1
                l += 1
                max_char = max(char_dict, key=char_dict.get)
                max_count = char_dict[max_char]
                replace_count = r - l + 1 - max_count

            longest = max(longest, r - l + 1)
            r += 1
        
        return longest
