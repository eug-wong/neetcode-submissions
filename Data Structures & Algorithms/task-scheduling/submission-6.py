class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        2 X's
        2 Y's

        X Y . X Y t=5 cycles
        Y X . Y X t=5 cycles

        We want to be greedy
        bottlenecked by the largest frequency task
        3 X's
        2 Y's -> always gonna want to consume X

        -> max-heap

        How do we keep track of our "cooldowns"?
        Queue = [[next_avail, task], [], []]

        tasks=["A","A","A","B","C"]
        n=3

        A B C - A - - - A
        '''

        heap = [] # -> minheap from python
        freq = Counter(tasks)
        for k, v in freq.items():
            heapq.heappush(heap, [-v, k])
        
        t = 1
        q = deque([])
        while q or heap:
            # handle pushing queue back onto heap
            while q and q[0][0] <= t:
                cur = q.popleft()
                heapq.heappush(heap, [cur[1], cur[2]])

            # handle popping and doing a task
            v, k = heapq.heappop(heap)
            if v + 1 < 0:
                q.append([t + n + 1, v + 1, k])

            if q and not heap:
                t = q[0][0]
            else:
                t += 1
        
        return t - 1