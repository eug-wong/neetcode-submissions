class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        intersects = defaultdict(int)
        for p, r in lights:
            l, r = p - r, p + r
            intersects[l] += 1
            intersects[r + 1] -= 1
        
        res = 0
        curr = 0
        brightest = 0
        for key in sorted(intersects):
            curr += intersects[key]
            if curr > brightest:
                brightest = curr
                res = key

        return res