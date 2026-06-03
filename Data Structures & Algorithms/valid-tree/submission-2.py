class Solution:
    from collections import defaultdict
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        cycle = False
        visited = set()
        def dfs(node, prev):
            nonlocal visited
            nonlocal cycle

            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                if neighbor not in visited:
                    dfs(neighbor, node)
                else:
                    cycle = True
                    return

            return
        
        dfs(0, -1)
        print(visited, n)
        return not cycle and len(visited) == n