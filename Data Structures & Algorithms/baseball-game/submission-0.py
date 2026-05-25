class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for operation in operations:
            if operation == "+":
                scores.append(scores[-1] + scores[-2])
            elif operation == "C":
                scores.pop()
            elif operation == "D":
                scores.append(2 * scores[-1])
            else:
                scores.append(int(operation))
            
        return sum(scores)