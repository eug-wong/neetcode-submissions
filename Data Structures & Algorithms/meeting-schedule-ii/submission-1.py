"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def checkRoom(self, l, r, room):
            for meeting in room:
                if meeting.start <= l < meeting.end or meeting.start < r <= meeting.end:
                    return False
            
            return True
    
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.end, reverse=True)
        rooms = []

        for interval in intervals:
            assigned = False
            for room in rooms:
                if self.checkRoom(interval.start, interval.end, room):
                    room.append(interval)
                    assigned = True
                    break
            if not assigned:
                rooms.append([interval])   

        return len(rooms)