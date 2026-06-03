class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        if we find the prefix and suffix arrays
        keeping track of max water at each height,
        find min of prefix and suffix and subtract the current height
        '''
        prefix = [0] * len(height)
        # prefix
        i = 0
        prev = 0
        while i < len(height):
            while i < len(height) and prev > height[i]:
                prefix[i] = prev
                i += 1
            
            if i < len(height):
                prev = height[i]
                prefix[i] = prev
                i += 1
        
        # suffix
        suffix = [0] * len(height)
        i = len(height) - 1
        prev = 0
        while i > 0:
            while i > 0 and prev > height[i]:
                suffix[i] = prev
                i -= 1
            
            if i > 0:
                prev = height[i]
                suffix[i] = prev
                i -= 1

        res = 0
        for i in range(len(suffix)):
            res += max(min(suffix[i], prefix[i]) - height[i], 0)
        
        return res
