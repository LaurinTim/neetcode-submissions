class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        l = 0
        l_best = 0
        r_best = len(s)

        t_count = dict()
        for letter in t:
            t_count[letter] = t_count.get(letter, 0) + 1

        match = 0
        count = dict()

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            if s[r] in t_count and t_count[s[r]] == count[s[r]]:
                match += 1

            while match == len(t_count):
                if r - l < r_best - l_best:
                    r_best = r
                    l_best = l
                
                if s[l] in t_count and count[s[l]] == t_count[s[l]]:
                    match -= 1
                
                count[s[l]] -= 1
                l += 1
            
        if r_best == len(s):
            return ""
        
        return s[l_best:r_best + 1]
