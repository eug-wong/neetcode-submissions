class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        choices = [x for x in range(1, n + 1)]
        res = []
        def backtrack(i, cur):
            nonlocal choices
            nonlocal res
            if len(cur) == k:
                res.append(cur)
                return

            if i == len(choices):
                return
            
            backtrack(i + 1, cur + [choices[i]])
            backtrack(i + 1, cur)

            return

        backtrack(0, [])
        return res