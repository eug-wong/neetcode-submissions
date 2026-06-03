from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashes = defaultdict(list)
        for s in strs:
            frequencies = [0] * 26
            for c in s:
                frequencies[ord(c) - 97] += 1
            hashes[tuple(frequencies)].append(s)
        return list(hashes.values())