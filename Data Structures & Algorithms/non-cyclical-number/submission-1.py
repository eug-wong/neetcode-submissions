class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            
            seen.add(n)
            s = str(n)
            n = 0
            for i in s:
                n += int(i)**2
        
        return True