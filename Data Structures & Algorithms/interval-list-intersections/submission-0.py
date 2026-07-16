class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        sweep = defaultdict(int)

        for l, r in firstList:
            sweep[l] += 1
            sweep[r + 1] -= 1
        
        for l, r in secondList:
            sweep[l] += 1
            sweep[r + 1] -= 1
        
        res = []
        cur = 0
        start = None
        for i in sorted(sweep):
            if cur == 2:
                res.append([start, i - 1])
            cur += sweep[i]
            start = i
        
        return res
