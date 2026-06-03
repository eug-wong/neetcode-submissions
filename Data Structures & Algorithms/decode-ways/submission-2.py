class Solution:
    def numDecodings(self, s: str) -> int:
        # it's dp... but how does dp apply to strings?
        # .. recursion seems like + memoization?
        # sort of like backtracking?
        # 2 choices:
        #   accept as solo decoding --> can't be a 0, also can't be solo if next is 0, if either element 0 accept as 2
        #   accept as two --> some constraints to handle - up to 26
        # 122204
        decodings = []

        def convert(num):
            return chr(64 + int(num))

        def dfs(i, cur):
            nonlocal decodings
            # print(i, cur)
            if i >= len(s):
                decodings.append(cur)
                return
            elif s[i] == '0':
                return

            # choice 1, accept as solo
            cur += convert(s[i])
            dfs(i + 1, cur)
            cur = cur[: len(cur) - 1]
            
            # choice 2, accept as duo
            if i < len(s) - 1 and int(s[i: i + 2]) < 27:
                cur += convert(s[i: i + 2])
                dfs(i + 2, cur)
            
            return
        
        dfs(0, "")
        
        return len(decodings)