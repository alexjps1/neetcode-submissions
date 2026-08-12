class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def op(operand: str) -> None:
            b = int(stack.pop())
            a = int(stack.pop())
            if operand == "+":
                res = a + b
            if operand == "-":
                res = a - b
            if operand == "/":
                res = a / b
            if operand == "*":
                res = a * b
            stack.append(int(res))


        for tok in tokens:
            if tok in ["+", "-", "*", "/"]:
                op(tok)
            else:
                stack.append(int(tok))
        return stack[0]