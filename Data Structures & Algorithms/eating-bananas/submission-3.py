class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        piles = [1, 2, 3, 250, 275, 500, 625, 750, 1000]
        k: 1 -> 1000
        500
        250
        '''

        l, r = 1, max(piles)
        lowest = r
        while l <= r:
            k = (l + r) // 2
            eats = 0
            for p in piles:
                eats += math.ceil(p/k)
            
            if eats <= h:
                lowest = k
                r = k - 1
            else:
                l = k + 1
        
        return lowest
            