class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        cur = intervals[0][1]
        remove = 0
        if len(intervals) == 1:
            return 0

        for interval in intervals[1: ]:
            l, r = interval

            if l < cur:
                remove += 1
                cur = min(cur, r)
            else:
                cur = r
        
        return remove