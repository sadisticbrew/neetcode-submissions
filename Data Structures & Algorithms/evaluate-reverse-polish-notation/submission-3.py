class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "+-*/"
        if len(tokens) == 1:
            return int(tokens[0])
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                elif token == "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif token == "*":
                    stack.append(stack.pop() * stack.pop())
                elif token == "/":
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(float(b) / a))
        return stack[0]