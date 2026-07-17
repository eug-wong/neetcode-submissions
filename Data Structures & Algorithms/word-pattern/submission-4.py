class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letters = set(pattern)
        words = s.split(" ")
        wordss = set(words)

        if len(wordss) != len(letters):
            return False
            
        mapping = {}
        for letter in pattern:
            for w in words:
                if w in mapping.values():
                    continue
                if letter not in mapping:
                    mapping[letter] = w
                    break

        # print(mapping)
        res = ""
        for c in pattern:
            res = res + mapping[c] + " "
        # print(res)
        return res[:-1] == s