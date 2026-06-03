class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def solve(running, index):
            if sorted(running) not in res:
                res.append(sorted(running.copy()))
            
            print(running, index)
            if index >= len(nums):
                return
            
            # choice 1: don't add and move on
            solve(running.copy(), index + 1)
            # choice 2: add and move on
            running.append(nums[index])
            solve(running.copy(), index + 1)
            return
        
        solve([], 0)
        return res