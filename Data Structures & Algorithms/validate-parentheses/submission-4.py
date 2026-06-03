class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        pairs = {
                "[": "]",
                "(": ")",
                "{": "}"
                }
        
        stack = []
        for i in range(len(s)):
            if stack and stack[-1] not in pairs:
                return False
            if stack and pairs[stack[-1]] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])

        print(stack)
        return len(stack) == 0
