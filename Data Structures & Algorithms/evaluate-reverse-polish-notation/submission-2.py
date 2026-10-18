class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ("+", "-", "*", "/")

        for val in tokens:
            if val in operators:
                pos = len(stack) - 2
                n1 = stack.pop(pos)
                n2 = stack.pop(pos)
                if val == "+":
                    res = n1 + n2
                elif val == "-":
                    res = n1 - n2
                elif val == "*":
                    res = n1 * n2
                else:
                    res = n1 / n2
                stack.append(int(res))
            else:
                stack.append(int(val))
        
        return stack[0]
        