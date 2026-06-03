class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for op in tokens:
            if op == "+":
                stack.append(stack.pop() + stack.pop())
            elif op == "-":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)
            elif op == "*":
                stack.append(stack.pop() * stack.pop())
            elif op == "/":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(float(num2) / num1))
            else:
                stack.append(int(op))
        
        return int(stack[0])