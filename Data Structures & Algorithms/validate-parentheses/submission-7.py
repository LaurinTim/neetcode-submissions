class Solution:
    def isValid(self, s: str) -> bool:
        match_dict = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        open_brackets = list()

        for l in s:
            if l in match_dict:
                open_brackets.append(l)
            elif l in match_dict.values():
                if (len(open_brackets) == 0
                    or match_dict[open_brackets[-1]] != l):
                    return False
                
                open_brackets.pop(-1)
        
        return len(open_brackets) == 0