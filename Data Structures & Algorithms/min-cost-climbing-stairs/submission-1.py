class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # recurrence relation: R(n) = min(R(n - 1), R(n - 2)) + cur cost
        # we can cache the min at any n index
        cost.append(0)
        cache = {}
        def recurse(i):
            if i == 0 or i == 1:
                return cost[i]
            
            if i in cache:
                return cache[i]

            cache[i] = min(recurse(i - 1), recurse(i - 2)) + cost[i]
            
            return cache[i]
        
        return recurse(len(cost) - 1)