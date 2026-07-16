class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegree = defaultdict(int)
        neighbours = defaultdict(list)
        for s, d in relations:
            indegree[d] += 1
            neighbours[s].append(d)
        
        # push all indegree 0 onto a queue
        q = deque()
        taken = set()
        for course in range(1, n + 1):
            if indegree[course] == 0:
                q.append(course)
                taken.add(course)
                
        # -- bfs, but only append indegree 0 nodes that are not yet visited onto the queue
        semesters = 0
        while q:
            semesters += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for nei in neighbours[cur]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0 and nei not in taken:
                        taken.add(nei)
                        q.append(nei)
        
        return semesters if len(taken) == n else -1