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
                cur.append("0")
                backtrack(i + 1, cur)
                cur.pop()
                return
            
            for j in range(i + 1, i + 4):
                if j <= len(s) and 0 <= int(s[i: j]) <= 255:
                    cur.append(s[i: j])
                    backtrack(j, cur)
                    cur.pop()
            
            return
        
        backtrack(0, [])
        return res