class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def solve(running):
            if len(running) == len(nums) and running not in res:
                res.append(running)
                return

            remaining = set(nums) - set(running)

            for num in remaining:
                running.append(num)
                solve(running.copy())
                running.pop()

        solve([])
        return res
        