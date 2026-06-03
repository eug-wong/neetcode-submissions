class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset = []
        def dfs(index):
            if index >= len(nums):
                res.append(subset.copy())
                return
            
            # decide to add current value
            subset.append(nums[index])
            dfs(index + 1)

            # decide not to append current value
            subset.pop()
            dfs(index + 1)

        dfs(0)
        return res