class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open  = {")": "(",
                         "}": "{",
                         "]": "["}
        for c in s:
            stack.append(c)

            if len(stack) > 1:
                if c in ["]", ")", "}"] and close_to_open[c] == stack[-2]:
                    stack.pop()
                    stack.pop()
        
        return False if stack else True