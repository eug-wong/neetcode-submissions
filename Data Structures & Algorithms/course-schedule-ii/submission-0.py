class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        neighbours = defaultdict(list)

        for s, d in prerequisites:
            indegree[s] += 1
            neighbours[d].append(s)
        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for neighbour in neighbours[cur]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
            
        return res if len(res) == numCourses else []
            