class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        hashmap = {}

        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]]+=1

            else:
                hashmap[s[i]]=1

        for i in range(len(s)):
            if t[i] in hashmap:
                if hashmap[t[i]]==0:
                    return False
                else:
                    hashmap[t[i]]-=1
            else:
                return False
        
        return True
                    