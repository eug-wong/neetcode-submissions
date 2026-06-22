class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        neighbours = defaultdict(list)

        for s, d in prerequisites:
            neighbours[d].append(s)

        def dfs(s):
            nonlocal visited
            nonlocal prerequisites
            visited.add(s)

            for neighbour in neighbours[s]:
                if neighbour not in visited:
                    dfs(neighbour)

        res = []
        for query in queries:
            visited = set()
            dfs(query[1])
            if query[0] in visited:
                res.append(True)
            else:
                res.append(False)
        
        return res

