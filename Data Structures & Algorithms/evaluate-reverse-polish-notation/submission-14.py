class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]
        for token in tokens:
            stack.append(token)
            if stack[-1] in operations:
                operation = stack.pop()
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if operation == "+":
                    stack.append(num1 + num2)
                
                elif operation == "*":
                    stack.append(num1 * num2)
                
                elif operation == "-":
                    stack.append(num1 - num2)
                
                elif operation == "/":
                    stack.append(math.trunc(num1/num2))
            # print(stack)
        
        return int(stack[-1])
