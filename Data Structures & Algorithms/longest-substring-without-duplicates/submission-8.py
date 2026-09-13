class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        l = 0
        r = 0
        long = 0
        seen = set()

        while r < len(s):
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1
            long = max(long, r - l)
            seen.remove(s[l])
            l += 1
        
        return long
        