class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        piles = [1, 2, 3, 250, 275, 500, 625, 750, 1000]
        k: 1 -> 1000
        500
        250
        '''

        k = max(piles)
        lower = 1
        lowest = k
        while lower <= k:
            mid = (k + lower) // 2
            eats = 0
            for i, pile in enumerate(piles):
                eats += math.ceil(pile/mid)
            
            if eats <= h:
                lowest = mid
                k = mid - 1
            else:
                lower = mid + 1
        
        return lowest