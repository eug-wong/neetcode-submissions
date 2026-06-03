class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()

        filtered = ""
        for c in s:
            if 97 <= ord(c) <= 122 or 48 <= ord(c) <= 57:
                filtered += c
            
        l, r = 0, len(filtered) - 1
        while l < r:
            if filtered[l] != filtered[r]:
                return False

            l += 1
            r -= 1
        
        return True