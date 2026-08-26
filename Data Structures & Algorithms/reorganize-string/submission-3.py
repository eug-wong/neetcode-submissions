class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = []
        for k, v in counts.items():
            heapq.heappush(heap, [-v, k])
        
        res = ""
        while heap:
            cur = heapq.heappop(heap)
            if res and cur[1] == res[-1]:
                if heap:
                    cur2 = heapq.heappop(heap)
                    res = res + cur2[1]
                    if cur2[0] + 1 < 0:
                        heapq.heappush(heap, [cur2[0] + 1, cur2[1]])
                    heapq.heappush(heap, cur)
                else:
                    return ""
            else:
                res = res + cur[1]
                if cur[0] + 1 < 0:
                    heapq.heappush(heap, [cur[0] + 1, cur[1]])
        
        return res
