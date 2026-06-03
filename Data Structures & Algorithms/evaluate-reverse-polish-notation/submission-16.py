class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # if token is an operation, evaluate
            if token in ["+", "-", "/", "*"]:
                # evaluate
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num2 - num1)
                elif token == "/":
                    stack.append(int(num2 / num1))
                else:
                    stack.append(num1 * num2)
            
            # if token is a number, push to stack
            else:
                stack.append(int(token))
        
        return stack[-1]