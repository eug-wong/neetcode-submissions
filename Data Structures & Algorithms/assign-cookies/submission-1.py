class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 7 8 9 10
        # i
        # 5 6 7 8
        # j

        # if s[j] >= g[i], increment both, res += 1
        # else increment j until we "match"
        g.sort()
        s.sort()

        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
                j += 1
            else:
                j += 1
        
        return i