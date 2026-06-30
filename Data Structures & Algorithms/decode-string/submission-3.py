class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "]":
                rep = ""
                while stack and stack[-1] != "[":
                    rep = rep + stack.pop()
                
                stack.pop()
                k = ""
                while stack and stack[-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    k = k + stack.pop()
                
                k, rep = int(k[::-1]), rep[::-1]
                stack = stack + list(rep) * k
            else:
                stack.append(c)
        
        return ''.join(stack)