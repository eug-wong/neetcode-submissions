class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        
        target = sum(matchsticks) // 4
        
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        def recurse(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]
            
            for side in range(4):
                if sides[side] + matchsticks[i] <= target:
                    sides[side] += matchsticks[i]
                    if recurse(i + 1):
                        return True
                    sides[side] -= matchsticks[i]

                if sides[side] == 0:
                    break
            
            return False

        return recurse(0)