class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        heap = []
        for k, v in freq.items():
            heap.append([-v, k])
        
        heapq.heapify(heap)
        res = ""
        while heap:
            save = 0
            if res and heap[0][1] == res[-1]:
                save = heapq.heappop(heap)
            
            if heap:
                cur = heapq.heappop(heap)
            else:
                return ""

            res = res + cur[1]
            if cur[0] + 1 < 0:
                heapq.heappush(heap, [cur[0] + 1, cur[1]])
            
            if save:
                heapq.heappush(heap, save)
        
        return res
            