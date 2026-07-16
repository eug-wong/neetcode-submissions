class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        l, r = 1, max(ribbons)
        res = 0
        while l <= r:
            cut = (l + r) // 2
            possible_ribbons = 0
            for ribbon in ribbons:
                possible_ribbons += ribbon // cut
            
            # print(cut, possible_ribbons)
            
            if possible_ribbons >= k:
                res = cut
                l = cut + 1
            else:
                r = cut - 1
        
        return res