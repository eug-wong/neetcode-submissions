class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        res = ""
        for s in strs:
            res = res + s + "こんにちは"
        
        return res

    def decode(self, s: str) -> List[str]:
        return s.split("こんにちは")[: -1]
