class Solution:
    def trap(self, height: List[int]) -> int:
        l = [0] * len(height)
        r = [0] * len(height)
        for i in range(len(height)):
            if i == 0:
                prevl = height[0]
                l[i] = 0
            if height[i] < prevl:
                l[i] = prevl - height[i]
            elif height[i] >= prevl:
                l[i] = 0
                prevl = height[i]

        for i in range(len(height) - 1, 0, -1):
            if i == len(height) - 1:
                prevr = height[-1]
                r[i] = 0
            if height[i] < prevr:
                r[i] = prevr - height[i]
            elif height[i] >= prevr:
                r[i] = 0
                prevr = height[i]
        
        out = [0] * len(height)
        for i in range(len(l)):
            out[i] = min(l[i], r[i])

        print(l, r)
        
        return sum(out)
            
        
