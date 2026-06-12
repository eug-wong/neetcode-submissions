class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse = 0
        cur = x
        while cur > 0:
            reverse = (reverse * 10) + (cur % 10)
            cur = cur // 10

        return reverse == x