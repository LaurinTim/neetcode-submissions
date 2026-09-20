class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_count = dict()
        matches = 0

        for val in s1:
            char_count[val] = char_count.get(val, 0) + 1
        
        for l in range(len(s2)):
            if s2[l] in char_count:            
                char_count[s2[l]] -= 1
                if char_count[s2[l]] >= 0:
                    matches += 1
            
            if matches == len(s1):
                return True
            
            if l >= len(s1) - 1 and s2[l - len(s1) + 1] in char_count:
                char_count[s2[l - len(s1) + 1]] += 1
                if char_count[s2[l - len(s1) + 1]] > 0:
                    matches -= 1
        
        return False
