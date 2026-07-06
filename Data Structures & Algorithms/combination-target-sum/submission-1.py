class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        def recurse(i, cur):
            nonlocal res
            if sum(cur) == target:
                res.add(tuple(cur))
                return

            if i == len(nums) or sum(cur) > target:
                return
            
            # accept
            recurse(i, cur + [nums[i]])
            # accept and move on
            recurse(i + 1, cur + [nums[i]])
            # reject and move on
            recurse(i + 1, cur)

            return

        recurse(0, [])
        return [list(x) for x in res]
                