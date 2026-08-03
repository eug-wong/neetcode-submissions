class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = [0] * 26
        buckets = defaultdict(list)
        for s in strs:
            for c in s:
                freq[ord(c) - 97] += 1
            
            buckets[tuple(freq)].append(s)
            freq = [0] * 26
        return list(buckets.values())