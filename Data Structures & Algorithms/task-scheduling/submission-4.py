class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        q = deque()
        freq = Counter(tasks)
        for k, v in freq.items():
            heapq.heappush(heap, [-v, k])
        
        t = 0
        while heap or q:
            while q and q[0][0] <= t:
                cur = q.popleft()
                heapq.heappush(heap, [cur[1], cur[2]])
            
            if heap:
                chosen = heapq.heappop(heap)
                if chosen[0] + 1 < 0: 
                    q.append([t + n + 1, chosen[0] + 1, chosen[1]])

            t += 1
            
        return t