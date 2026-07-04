class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        #     12
        #  2  6    3  4   4  3   6  2   
        #  2  2  3              2 3
        
        # [12]
        # [2, 6] - add to res
        # [2, 2, 3] - add to res
        # reach base case wehre all are unfactorable, end recursion there

        # O(n^something...?)
        # space O(n^something)
        res = []
        def recurse(cur):
            nonlocal res
            if len(cur) > 1:
                res.append(cur.copy())

            last = cur.pop()
            i = 2 if not cur else cur[-1]

            while i <= last // i:
                if last % i == 0:
                    cur.append(i)
                    cur.append(last // i)
                    recurse(cur)
                    cur.pop()
                    cur.pop()
                i += 1
            
            cur.append(last)
        
        recurse([n])
        return res
                        
            