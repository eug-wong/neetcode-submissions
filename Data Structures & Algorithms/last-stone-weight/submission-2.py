class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            if s1 == s2:
                continue
            elif s1 < s2:
                heapq.heappush(stones, s1 - s2)
            else:
                heapq.heappush(stones, s2 - s1)
        
        return -1 * stones[-1] if stones else 0