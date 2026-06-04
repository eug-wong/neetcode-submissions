class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
                    '2': ['A', 'B', 'C'],
                    '3': ['D', 'E', 'F'], 
                    '4': ['G', 'H', 'I'],
                    '5': ['J', 'K', 'L'],
                    '6': ['M', 'N', 'O'],
                    '7': ['P', 'Q', 'R', 'S'],
                    '8': ['T', 'U', 'V'],
                    '9': ['W', 'X', 'Y', 'Z']
                }
        res = []
        def backtrack(cur, i):
            nonlocal mapping
            nonlocal res
            if i == len(digits):
                res.append(cur.lower())
                return
            
            for c in mapping[digits[i]]:
                backtrack(cur + c, i + 1)

            return
        
        backtrack("", 0)
        
        return res if res[-1] != "" else []