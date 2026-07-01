class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strings:
            diffs = tuple()
            i = ord(s[0])
            for c in s:
                diffs += ((i - ord(c)) % 26,)

            group[diffs].append(s)
        
        return list(group.values())