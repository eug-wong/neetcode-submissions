class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [x * -1 for x in stones]
        heapq.heapify(stones)

        # O(1) pop time for each of two stones
        # O(log n) push back onto heap
        # O(n log n)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 == stone2:
                continue
            elif stone1 < stone2:
                heapq.heappush(stones, stone1 - stone2)
            else:
                heapq.heappush(stones, stone2 - stone1)
        
        return heapq.heappop(stones) * -1 if stones else 0
