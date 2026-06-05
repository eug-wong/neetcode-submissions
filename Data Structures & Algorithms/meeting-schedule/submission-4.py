"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # [(0, 10), (10, 20)] -> combine to (0, 20)
        # [(0, 10), (5, 10)] -> return False
        # if we finish processing entire list -> return True
        intervals = sorted(intervals, key=lambda x: x.start)

        if len(intervals) <= 1:
            return True
            
        cur = intervals[0]
        
        for interval in intervals[1: ]:
            l, r = interval.start, interval.end
            if cur.start <= l < cur.end:
                return False
            
            cur.end = max(cur.end, r)
        
        return True