class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def solve (running, index, tot):

            # base cases
            if (tot == target):
                if running not in res:
                    res.append(running.copy())
            
            if (index >= len(nums) or tot > target):
                return

            running.append(nums[index])
            solve(running, index, tot + nums[index])
            running.pop()
            solve(running, index + 1, tot)

        solve ([], 0, 0)
        return res