class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        heap = []
        people = 0
        heapq.heapify(heap)
        for trip in trips:
            while heap and heap[0][0] <= trip[1]:
                people -= heapq.heappop(heap)[1]
            
            if people + trip[0] > capacity:
                return False
            
            people += trip[0]
            heapq.heappush(heap, [trip[2], trip[0]])
        
        return True
