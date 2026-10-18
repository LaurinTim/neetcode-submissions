class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ("+", "-", "*", "/")

        for val in tokens:
            if val in operators:
                n2 = stack.pop()
                n1 = stack.pop()
                if val == "+":
                    stack.append(n1 + n2)
                elif val == "-":
                    stack.append(n1 - n2)
                elif val == "*":
                    stack.append(n1 * n2)
                else:
                    stack.append(int(n1 / n2))
            else:
                stack.append(int(val))
        
        return stack.pop()
        