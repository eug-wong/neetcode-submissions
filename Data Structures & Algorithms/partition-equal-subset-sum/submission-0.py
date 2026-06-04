class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # [1, 2, 3, 4]
        # select elements to add up to half of sum, so 10/2 = 5
        # if we can select a subset of elements that add up to 5, return True
        # otherwise, return False

        # can use backtrack as well.... but would cost 2^n worst case, memoize?
        # reach target 5, return True
        # 
        def backtrack(cur, i, target):
            nonlocal memo
            if cur == target:
                return True
            if i == len(nums):
                return False
            
            if (cur, i) in memo.keys():
                return memo[(cur, i)]
            
            res = backtrack(cur, i + 1, target) or backtrack(cur + nums[i], i + 1, target)
            memo[(cur, i)] = res

            return res
        
        memo = {}
        
        return backtrack(0, 0, sum(nums)/2)