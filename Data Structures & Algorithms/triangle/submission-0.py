class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 2^n backtrack, not great
        # dp -> cache row : lowest_sum_so_far
        rows = len(triangle)
        cache = {}
        def recurse(r, c):
            if r == rows:
                return 0
            
            if (r, c) in cache:
                return cache[(r, c)]
            
            # 2 choices, cur or cur + 1
            res = triangle[r][c] + min(recurse(r + 1, c), recurse(r + 1, c + 1))

            cache[(r, c)] = res

            return res

        return recurse(0, 0)