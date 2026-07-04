class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def backtrack(i, cur):
            nonlocal res
            if i == len(nums):
                t = 0
                for n in cur:
                    t = t ^ n
                res += t
                return
            
            # accept into cur
            cur.append(nums[i])
            backtrack(i + 1, cur)
            cur.pop()

            backtrack(i + 1, cur)
        
        backtrack(0, [])
        return res
            