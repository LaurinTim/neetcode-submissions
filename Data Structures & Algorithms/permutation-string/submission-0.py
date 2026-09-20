class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_count = defaultdict(int)
        min_count = 0

        for val in s1:
            char_count[val] += 1
        
        for l in range(len(s2)):
            if l < len(s1) - 1:
                char_count[s2[l]] -= 1
                continue
            
            char_count[s2[l]] -= 1
            min_count = min([val for val in char_count.values()])
            if min_count == 0:
                return True
                
            char_count[s2[l - len(s1) + 1]] += 1
        
        return False
        