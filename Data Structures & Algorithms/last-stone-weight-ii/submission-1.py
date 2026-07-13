class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {}
        total = sum(stones)
        def backtrack(i, cur):
            if i == len(stones) or cur >= total:
                return abs(cur - (total - cur))
            
            if (i, cur) in dp:
                return dp[(i, cur)]
            
            dp[(i, cur)] = min(backtrack(i + 1, cur), backtrack(i + 1, cur + stones[i]))
            
            return dp[(i, cur)]
        
        return backtrack(0, 0)
            

            
