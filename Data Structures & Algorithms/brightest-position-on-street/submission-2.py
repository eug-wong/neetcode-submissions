class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        # insight: we only care about checking the end points of each light interval
        # if two lights overlap at some index, then it may or may not overlap within the interval
        # so optimum is always at edge of intervals

        brightness = defaultdict(int)
        for pos, ran in lights:
            brightness[pos - ran] += 1
            brightness[pos + ran + 1] -= 1
        
        # print(lights)

        res = [0, 0]
        cur = 0
        for i, v in sorted(brightness.items()):
            cur += v
            # print(i, cur)
            if cur > res[1]:
                res = [i, cur]
        
        return res[0]