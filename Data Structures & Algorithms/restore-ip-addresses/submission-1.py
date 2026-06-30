class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(i, cur):
            if len(cur) > 4:
                return
                
            if i == len(s):
                if len(cur) == 4:
                    res.append(".".join(cur))
                return
            
            if s[i] == "0":
                backtrack(i + 1, cur + ["0"])
                return
            
            for j in range(i + 1, i + 4):
                if j <= len(s) and 0 <= int(s[i: j]) <= 255:
                    backtrack(j, cur + [s[i: j]])
            
            return
        
        backtrack(0, [])
        return res