class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")

        cleaned = ""
        for char in s:
            if (ord(char) >= 97 and ord(char) < 123) or(ord(char) >= 48 and ord(char) < 58):
                cleaned += char

        if len(cleaned) % 2 == 1:
            cleaned = cleaned[0: len(cleaned)//2] + cleaned[len(cleaned)//2 + 1: ]

        print(cleaned)
        stack = []
        for i in range(len(cleaned)):
            char = cleaned[i]
            if i < len(cleaned)/2:
                stack.append(char)
            elif char == stack[-1]:
                stack.pop()
        
        return len(stack) == 0