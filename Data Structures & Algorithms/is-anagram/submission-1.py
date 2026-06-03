class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1, dict2 = {}, {}

        for c in s:
            dict1[c] = 1 + dict1.get(c, 0)
        
        for c in t:
            dict2[c] = 1 + dict2.get(c, 0)
        
        return dict2 == dict1