class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [[task[0], task[1], i] for i, task in enumerate(tasks)]
        tasks.sort(key=lambda x: x[0])
        tasks = deque(tasks)
        t = 0
        heap = []
        res = []
        while tasks or heap:
            while tasks and tasks[0][0] <= t:
                cur = tasks.popleft()
                heapq.heappush(heap, [cur[1], cur[2]])
            
            if heap:
                process = heapq.heappop(heap)
                t += process[0]
                res.append(process[1])
            else:
                t = tasks[0][0]
        
        return res