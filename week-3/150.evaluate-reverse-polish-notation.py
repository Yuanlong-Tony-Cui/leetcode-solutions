class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = {'+', '-', '*', '/'}

        def compute(a: str, b: str, operator: str) -> str:
            # print(a, operator, b)
            if operator == '+':
                return int(a) + int(b)
            if operator == "-":
                return int(a) - int(b)
            if operator == "*":
                return int(a) * int(b)
            if operator == "/":
                res: float = int(a) / int(b)
                return math.floor(res) if res > 0 else math.ceil(res)
        
        # Resolve from inside to outside
        stack = []
        for token in tokens:
            if token in operators:
                num2 = stack.pop(-1)
                num1 = stack.pop(-1)
                stack.append(str(compute(num1, num2, token)))
            else:  # an integer
                stack.append(token)

        return int(stack[-1])
