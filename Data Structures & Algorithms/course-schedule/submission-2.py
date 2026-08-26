class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        neighbours = defaultdict(list)
        for s, d in prerequisites:
            indegree[s] += 1
            neighbours[d].append(s)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        taken = 0
        while q:
            for nei in neighbours[q.popleft()]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            taken += 1

        return taken == numCourses