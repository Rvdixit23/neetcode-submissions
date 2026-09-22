class Solution:
    def calPoints(self, operations: List[str]) -> int:
        solution = []
        for op in operations:
            if op == "C":
                solution.pop()
            elif op == "D":
                solution.append(solution[-1] * 2)
            elif op == "+":
                solution.append(int(solution[-1]) + int(solution[-2]))
            else:
                solution.append(int(op))

        return sum(solution)