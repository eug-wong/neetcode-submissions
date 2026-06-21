class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # first iterate until you find a spot
        spot = len(intervals)
        res = []
        for i, interval in enumerate(intervals):
            if ((interval[0] <= newInterval[0] <= interval[1] or interval[0] <= newInterval[1] <= interval[1])
                or (interval[0] >= newInterval[0])):
                spot = i - 1
                break
            else:
                res.append(interval)
            

        # from there, combine overlapping intervals until end of list.
        res.append(newInterval)
        for i in range(spot + 1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= res[-1][0] <= interval[1] or interval[0] <= res[-1][1] <= interval[1] or res[-1][0] <= interval[0] <= res[-1][1]:
                res[-1] = [min(res[-1][0], interval[0]), max(res[-1][1], interval[1])]
            else:
                res.append(interval)

        # time O(n), space O(n), need some res array...
        return res
        