class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def allPalindromes(arr):
            for s in arr:
                if s[::-1] != s:
                    return False

            return True

        def backtrack(i, cur):
            if i == len(s):
                if allPalindromes(cur):
                    res.append(cur)
                return
            
            # make new
            backtrack(i + 1, cur + [s[i]])

            # add to current
            if cur:
                cur[-1] = cur[-1] + s[i]
                backtrack(i + 1, cur)

            return
        
        backtrack(0, [])
        return res
        
