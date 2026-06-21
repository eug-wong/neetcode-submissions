class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {}
        neighbours = defaultdict(list)

        for n in range(numCourses):
            indegree[n] = 0

        for a, b in prerequisites:
            neighbours[b].append(a)
            indegree[a] += 1
        
        q = deque([])
        for k, v in indegree.items():
            if v == 0:
                q.append(k)
        
        while q:
            cur = q.popleft()
            for n in neighbours[cur]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        
        return sum(indegree.values()) == 0
        
