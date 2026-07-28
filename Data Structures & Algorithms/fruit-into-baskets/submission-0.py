class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = defaultdict(int)
        l, r = 0, 0
        total = 0
        while r < len(fruits):
            baskets[fruits[r]] += 1
            while l < r and len(baskets) > 2:
                baskets[fruits[l]] -= 1
                if not baskets[fruits[l]]:
                    baskets.pop(fruits[l])
                l += 1
            
            total = max(total, sum(baskets.values()))
            r += 1
        
        return total
            

            