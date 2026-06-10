class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        
        visited = set(deadends)
        if "0000" in visited:
            return -1
        
        q = deque(["0000"])
        visited.add("0000")
        steps = 0

        while q:
            steps += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for i in range(4):
                    for j in [-1, 1]:
                        digit = str((int(cur[i]) + j + 10) % 10)
                        nextt = cur[: i] + digit + cur[i + 1: ]
                        if nextt in visited:
                            continue
                        if nextt == target:
                            return steps
                        q.append(nextt)
                        visited.add(nextt)
        
        return -1