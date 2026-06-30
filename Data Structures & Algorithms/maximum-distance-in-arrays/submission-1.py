class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # consider case where switching index is actually good
        minn = [float('inf'), 0]
        maxx = [float('-inf'), 0]
        res = 0
        for i, a in enumerate(arrays):
            res = max(res, maxx[0] - a[0], a[-1] - minn[0])

            if minn[0] > a[0]:
                minn = [a[0], i]
            if maxx[0] < a[-1]:
                maxx = [a[-1], i]
            
            if maxx[1] != minn[1]:
                res = max(res, maxx[0] - minn[0])
            

            
        return res