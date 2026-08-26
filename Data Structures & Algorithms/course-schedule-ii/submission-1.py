class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # possible to have cyclical dependency
        # preqrequisites = [[1, 0], [2, 0], [3, 2]]
        # 3 <- 2 <- 0
        #     1 <__|
        # kahns top sort
        indegree = defaultdict(int)
        neighbours = defaultdict(list)
        for s, d in prerequisites:
            indegree[s] += 1
            neighbours[d].append(s)
        
        # bfs
        q = deque()

        # populate q w/ already indegree 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        res = []
        while q:
            cur = q.popleft()
            for nei in neighbours[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            res.append(cur)
        
        return res if len(res) == numCourses else []