class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq1, freq2 = Counter(ransomNote), Counter(magazine)
        for k, v in freq1.items():
            if freq1[k] > freq2[k]:
                return False
        
        return True