class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0] * len(words)
        vowels = set(["a", "e", "i", "o", "u"])
        cur = 0
        for i, s in enumerate(words):
            if s[0] in vowels and s[-1] in vowels:
                cur += 1
            
            prefix[i] = cur
        
        print(prefix)
        res = []
        for query in queries:
            l, r = query
            res.append(prefix[r] - prefix[l - 1]) if l > 0 else res.append(prefix[r])

        return res