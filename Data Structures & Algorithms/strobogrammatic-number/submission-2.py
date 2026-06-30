class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strob = {"6": "9", "9": "6", "1": "1", "0": "0", "8": "8"}
        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] not in strob or num[r] not in strob:
                return False
            
            if strob[num[l]] != num[r]:
                return False

            l += 1
            r -= 1
        
        return True