class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        deny_R = 0
        deny_D = 0
        q = deque()
        for c in senate:
            q.append(c)
        
        freq = Counter(senate)

        while q and freq["R"] > 0 and freq["D"] > 0:
            c = q.popleft()
            if c == "R":
                if deny_R > 0:
                    deny_R -= 1
                    freq["R"] -= 1
                    continue
                else:
                    deny_D += 1
                    q.append("R")
            
            if c == "D":
                if deny_D > 0:
                    deny_D -= 1
                    freq["D"] -= 1
                    continue
                else:
                    deny_R += 1
                    q.append("D")
        
        return "Radiant" if freq["D"] == 0 else "Dire"