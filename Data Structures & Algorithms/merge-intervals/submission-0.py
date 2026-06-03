class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = [intervals[0]]

        for cur in intervals[1: ]:
            prev = res.pop()
            i1 = min(prev, cur)
            i2 = max(prev, cur)
            if i1[0] <= i2[0] <= i1[1]:
                res.append([i1[0], max(i1[1], i2[1])])
            else:
                res.append(prev)
                res.append(cur)
        
        return res