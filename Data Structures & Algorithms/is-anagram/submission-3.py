class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hash = {}
        for letter in s:
            if letter in s_hash:
                s_hash[letter] += 1
            else: s_hash[letter] = 1
        for letter in t:
            if letter in s_hash:
                s_hash[letter] -= 1
                if s_hash[letter] < 0:
                    return False
            else:
                return False
        return True
        