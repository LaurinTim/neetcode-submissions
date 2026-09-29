class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        l, r = 0, 0
        l_best, r_best = 0, len(s)
        count = dict()
        match = 0

        t_count = dict()
        for letter in t:
            t_count[letter] = t_count.get(letter, 0) + 1
        
        for l in range(len(s) - len(t) + 1):
            if s[l] in t_count:
                r = max(r, l)
                while r < len(s) and match < len(t):
                    count[s[r]] = count.get(s[r], 0) + 1
                    if s[r] in t_count and count[s[r]] <= t_count[s[r]]:
                        match += 1

                    r += 1

                if match == len(t) and (r - l - 1) < (r_best - l_best):
                    l_best = l
                    r_best = r - 1
                
                if r == len(s) and match < len(t):
                    break
            
            if s[l] in t_count and count[s[l]] <= t_count[s[l]]:
                match -= 1

            count[s[l]] = count.get(s[l], 0) - 1
            l += 1

        if r_best == len(s):
            return ""
        
        return s[l_best:r_best + 1]
            

