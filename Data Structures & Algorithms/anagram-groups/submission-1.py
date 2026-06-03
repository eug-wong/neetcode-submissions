from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            print(freq)
            for c in s:
                freq[ord(c) - 97] += 1
            
            groupings[tuple(freq)].append(s)

        return list(groupings.values())
