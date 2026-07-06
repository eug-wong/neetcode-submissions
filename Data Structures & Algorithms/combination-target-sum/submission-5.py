class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()
        def recurse(i, cur):
            nonlocal res
            if sum(cur) == target:
                res.add(tuple(cur))
                return

            if i == len(nums) or sum(cur) > target:
                return
            
            # accept
            cur = cur + [nums[i]]
            recurse(i, cur)
            cur.pop()
            # reject and move on
            recurse(i + 1, cur)
            return

        recurse(0, [])
        return [list(x) for x in res]
                