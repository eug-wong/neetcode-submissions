class Solution:
    def longestPalindrome(self, s: str) -> str:
        # a b a b d
        # what is the dp?
        # we can keep track of whether a substring i:j is a palindrome given
        # some dp[i][j] = true
        # dp[i][j] is a palindrome if dp[i - 1][j - 1] == true and s[i] == s[j]
        # if palindrome then update res?
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res_i, res_j = 0, 0
        # [[T 0 0 0 0]
        #  [F T 0 0 0]
        #. [T 0 T 0 0]
        #. [F 0 0 T 0]
        #. [F 0 0 0 T]]
        # a
        # ababd
        # increment i, now go j = i incrementu pwards
        # 1, 3
        # assuming we have that set up, i think we can just begin testing it?
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                    if j - i + 1 > res_j - res_i + 1:
                        res_i = i
                        res_j = j
                        print(res_i, res_j)

        return s[res_i: res_j + 1]