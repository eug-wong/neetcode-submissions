class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def solve (running, index, tot):

            # base cases
            if (tot == target):
                if sorted(running) not in res:
                    res.append(sorted(running.copy()))
            
            if (index >= len(candidates) or tot > target):
                return

            running.append(candidates[index])
            solve(running, index + 1, tot + candidates[index])
            running.pop()
            solve(running, index + 1, tot)

        solve ([], 0, 0)
        return res