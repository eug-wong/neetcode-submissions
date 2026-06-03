class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # brute force, iterate through intervals and find min length query
        # O(n x m)

        res = []
        for query in queries:
            min_length = float('inf')
            # min_length length and index
            for i, interval in enumerate(intervals):
                length = interval[1] - interval[0] + 1
                if interval[0] <= query <= interval[1]:
                    min_length = min(length, min_length)

            res.append(min_length)
        
        return [x if x != float('inf') else -1 for x in res]
