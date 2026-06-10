class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        prereqOf = defaultdict(list)

        for p in prerequisites:
            indegree[p[0]] += 1
            prereqOf[p[1]].append(p[0])
        
        q = deque([])
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                for c in prereqOf[cur]:
                    indegree[c] -= 1
                    if indegree[c] == 0:
                        q.append(c)
        
        return sum(indegree.values()) == 0