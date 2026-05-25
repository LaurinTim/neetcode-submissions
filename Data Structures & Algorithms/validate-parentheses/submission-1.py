class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = []
        for symbol in s:
            if symbol == "(":
                open_brackets.append('(')
            elif symbol == "{":
                open_brackets.append('{')
            elif symbol == "[":
                open_brackets.append('[')
            elif not open_brackets:
                return False
            else:
                last_open = open_brackets.pop()
                if last_open == '(' and symbol != ')':
                    return False
                elif last_open == '[' and symbol != ']':
                    return False
                if last_open == '{' and symbol != '}':
                    return False
            
        return not open_brackets