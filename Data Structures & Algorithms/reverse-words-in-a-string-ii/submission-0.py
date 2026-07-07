class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse
        l, r = 0, len(s) - 1
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
        

        # then everytime we hit space or reach the end, reverse that
        r = 0
        l = 0
        while r < len(s):
            while r < len(s) and s[r] != " ":
                r += 1
            
            t = r
            r -= 1
            while l <= r:
                s[l], s[r] = s[r], s[l]
                l, r = l + 1, r - 1

            l, r = t + 1, t + 1