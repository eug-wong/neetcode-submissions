class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        neighbours = defaultdict(set)
        idx = {}
        for account in accounts:
            name = account[0]
            emails = account[1: ]
            for email in emails:
                neighbours[email].update(emails)
                idx[email] = name
                
        def dfs(start):
            nonlocal visited
            nonlocal same
            same.append(start)
            visited.add(start)

            for neighbour in neighbours[start]:
                if neighbour not in visited:
                    dfs(neighbour)
            
            return

        res = []
        visited = set()
        for email in idx.keys():
            if email in visited:
                continue
            same = []
            dfs(email)
            res.append([idx[email]] + sorted(same))
        
        return res

