class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # catsincars
        # 2 choices:
        # cat -> sin -> car -> s?
        # cats -> in -> car -> s?
        # so there's m choices at every branch worst case so o(n^m) w/ backtracking
        # use dp as well, memoization?
        # for example
        # cat -> sin -> car -> s?
        # cats -> in -> car -> s?
        #             ^ at this point, no need to recalculate what happens to cars
        #               since both branches are at the same index, just store it once and pull after?
        # what does the basic backtracking implementation look like
        # how does the recursion work...? 
        memo = {len(s): True}
        def backtrack(i):
            nonlocal memo
            nonlocal s
            nonlocal wordDict

            if i in memo.keys():
                return memo[i]

            res = False
            for word in wordDict:
                n = len(word)
                if i + n <= len(s) and s[i: i + n] == word:
                    # print("checking: ", word, s[i: i + n])
                    res = res or backtrack(i + n)
                
            memo[i] = res
            return res
        
        print(memo)
        
        return backtrack(0)
        
