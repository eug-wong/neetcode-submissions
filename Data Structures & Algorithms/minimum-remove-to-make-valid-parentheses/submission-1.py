class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        opens = 0
        for c in s:
            if c == "(":
                stack.append(c)
                opens += 1
            elif c == ")" and opens > 0:
                stack.append(c)
                opens -= 1
            elif c != ")":
                stack.append(c)
        
        res = []
        for c in reversed(stack):
            if c == "(" and opens > 0:
                opens -= 1
            else:
                res.append(c)

        return "".join(reversed(res))