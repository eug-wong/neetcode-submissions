class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # first thing to consider is we always want to do the most common task
        # keep track of the number of each task in dict
        # want the most, so use minheap * -1 to keep track of most common
        # use a queue to keep track of "cooldown"
        # next time until available? ... so if we accept
        # X at t=0, we can expect to use x again at t=3
        # q = [(X, 3)]
        # algorithm:
        #       while q:
        #           pop off from heap until we find most frequent
        freq = Counter(tasks)
        q = deque()
        h = []
        for k, v in freq.items():
            h.append([-1 * v, k])
        heapq.heapify(h)

        t = 0
        while h or q:
            # reintroduce item on queue if cooldown is over
            while q and q[0][0] < t:
                heapq.heappush(h, [-1 * freq[q[0][1]], q[0][1]])
                q.popleft()

            # use most frequent
            if h:
                task = heapq.heappop(h)
                freq[task[1]] -= 1
                if freq[task[1]] > 0:
                    q.append([t + n, task[1]])
        
            
            t += 1

        return t
