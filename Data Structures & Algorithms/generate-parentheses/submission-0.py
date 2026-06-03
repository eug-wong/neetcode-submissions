class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 3 cases to consider
        # 1. n == opens == closes --> valid parantheses, add to output
        # 2. opens < n --> add an opening parentheses
        # 3. opens > closes --> add a closing parentheses
        stack = []
        out = []

        def backtrack(opens, closes):
            if n == opens == closes:
                out.append("".join(stack))
                return
            
            if opens < n:
                stack.append("(")
                backtrack(opens + 1, closes)
                stack.pop()

            if opens > closes:
                stack.append(")")
                backtrack(opens, closes + 1)
                stack.pop()

        backtrack(0,0)
        return out