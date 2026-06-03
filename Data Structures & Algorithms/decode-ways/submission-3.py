class Solution:
    def numDecodings(self, s: str) -> int:
        # it's dp... but how does dp apply to strings?
        # .. recursion seems like + memoization?
        # sort of like backtracking?
        # 2 choices:
        #   accept as solo decoding --> can't be a 0, also can't be solo if next is 0, if either element 0 accept as 2
        #   accept as two --> some constraints to handle - up to 26
        # 122204
        # now need memoization... i think?
        # what can we keep track of? basically previously calculated decodings right
        # 
        memo = {len(s): 1}

        def dfs(i):
            if i in memo:
                return memo[i]
            elif s[i] == '0':
                return 0

            # choice 1, accept as solo
            res = dfs(i + 1)
            
            # choice 2, accept as duo
            if i < len(s) - 1 and int(s[i: i + 2]) < 27:
                res += dfs(i + 2)
            
            memo[i] = res
            
            return res
        
        return dfs(0)