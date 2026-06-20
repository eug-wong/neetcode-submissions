class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # just djikstras, find the last time
        # djikstras is just bfs + priority queue (heap) sorted by min time i think
        neighbours = defaultdict(list)
        min_times = defaultdict(lambda: float('inf'))
        visited = set()
        for s, d, t in times:
            neighbours[s].append([t, d])

        q = []
        heapq.heapify(q)
        heapq.heappush(q, [0, k])
        min_times[k] = 0

        while q:
            t, d = heapq.heappop(q)
            if d in visited:
                continue
            visited.add(d)

            for t1, d1 in neighbours[d]:
                if t + t1 < min_times[d1]:
                    min_times[d1] = t + t1
                    heapq.heappush(q, [t + t1, d1])
        
        print(min_times)
        
        return max(min_times.values()) if len(min_times.values()) == n else -1