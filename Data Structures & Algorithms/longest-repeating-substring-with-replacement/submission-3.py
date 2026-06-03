class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        "AAABABB"
         l
         r
        
        # of k replacements is the (r - l + 1) - maximum frequency in window
        # if exceeds k, we must pop
        # use array of size 26, so finding max is constant time
        # O(n)
        '''
        if len(s) == 0:
            return 0

        freq = [0] * 26
        l, r = 0, 0
        res = 1
        while r < len(s):
            freq[ord(s[r]) - 65] += 1
            while l <= r and r - l + 1 - max(freq) > k:
                freq[ord(s[l]) - 65] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return res