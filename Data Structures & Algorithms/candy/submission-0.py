class Solution:
    def candy(self, ratings: List[int]) -> int:
        # monotonic sweep -> and <- ?
        prev = [0, 0]
        candies = [0] * len(ratings)
        for i, r in enumerate(ratings):
            if r > prev[0]:
                candies[i] = prev[1] + 1
                prev = [r, prev[1] + 1]
            else:
                candies[i] = 1
                prev = [r, 1]
        
        prev = [0, 0]
        for i in range(len(ratings) - 1, -1, -1):
            if ratings[i] > prev[0]:
                candies[i] = max(candies[i], prev[1] + 1)
                prev = [ratings[i], prev[1] + 1]
            else:
                candies[i] = max(candies[i], 1)
                prev = [ratings[i], 1]

        return sum(candies)
