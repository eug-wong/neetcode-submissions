class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a:
            heap.append([-a, "a"])
        if b:
            heap.append([-b, "b"])
        if c:
            heap.append([-c, "c"])
        heapq.heapify(heap)

        s = ""

        while heap:
            temp = None
            if len(s) >= 2 and heap[0][1] == s[-1] and heap[0][1] == s[-2]:
                temp = heapq.heappop(heap)
            
            if heap:
                count, c = heapq.heappop(heap)
            else:
                break

            s = s + c
            if count + 1 < 0:
                heapq.heappush(heap, [count + 1, c])
            
            if temp:
                heapq.heappush(heap, temp)
        
        return s
