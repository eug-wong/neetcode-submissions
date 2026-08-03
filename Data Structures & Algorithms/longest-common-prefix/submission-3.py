class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        buckets = defaultdict(set)
        for s in strs:
            for i, c in enumerate(s):
                buckets[i].add(c)
        
        res = ""
        for i in range(min([len(x) for x in strs])):
            if len(buckets[i]) == 1:
                res = res + str(list(buckets[i])[0])
            else:
                break
        
        return res