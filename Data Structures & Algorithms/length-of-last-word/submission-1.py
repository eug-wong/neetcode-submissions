class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        res = ""
        for word in words:
            if word:
                res = word
        
        return len(res)