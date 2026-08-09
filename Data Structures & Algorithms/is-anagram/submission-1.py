class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hash = dict()
        t_hash = dict()
        for i in range(len(s)):
            if s[i] in s_hash:
                s_hash[s[i]] += 1
            else:
                s_hash[s[i]] = 1
            
            if t[i] in t_hash:
                t_hash[t[i]] += 1
            else:
                t_hash[t[i]] = 1
        
        for letter in s_hash:
            if letter not in t_hash or s_hash[letter] != t_hash[letter]:
                return False
            
        return True