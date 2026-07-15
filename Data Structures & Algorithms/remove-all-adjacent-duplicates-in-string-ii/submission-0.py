class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if k == 1:
            return ""

        res = []
        for c in s:
            res.append(c)
            if len(res) >= k and len(set(res[-k: ])) == 1:
                for _ in range(k):
                    res.pop()
        
        return "".join(res)