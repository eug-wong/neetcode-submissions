class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        options = defaultdict(list)
        for flight in flights:
            f, t, p = flight
            options[f].append([t, p])
        
        heap = [[0, src, 0]]
        heapq.heapify(heap)
        visited = {}
        while heap:
            cur, s, stops = heapq.heappop(heap)
            if s == dst:
                return cur
            if stops > k or visited.get(s, float('inf')) <= stops:
                continue
            visited[s] = stops
            for option in options[s]:
                heapq.heappush(heap, [cur + option[1], option[0], stops + 1])

        return -1