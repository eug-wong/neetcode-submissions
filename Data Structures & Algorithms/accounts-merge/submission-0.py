class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        neighbours = defaultdict(set)
        for account in accounts:
            name = account[0]
            emails = account[1: ]
            for email in emails:
                neighbours[email].update(emails)
        
        def dfs(start):
            nonlocal visited
            nonlocal same
            if start in visited:
                return
            
            same.append(start)
            visited.add(start)

            for neighbour in neighbours[start]:
                dfs(neighbour)
            
            return

        res = []
        for account in accounts:
            name = account[0]
            emails = account[1: ]
            visited = set()
            same = []
            dfs(emails[0])

            if [name] + sorted(same) not in res:
                res.append([name] + sorted(same))
        
        return res

