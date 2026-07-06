class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k

        memo = defaultdict(bool)
        def backtrack(i, cur):
            # cur is array of 0's, where each index represents a subset's sum
            if i == len(nums):
                # do a check to see if sums are equivalent
                return len(set(cur)) == 1
            
            hashkey = tuple(sorted(cur))
            if (i, hashkey) in memo:
                return memo[(i,hashkey)]
            
            res = False
            for j in range(len(cur)):
                if cur[j] + nums[i] > target:
                    continue
                cur[j] += nums[i]
                res = res or backtrack(i + 1, cur)
                cur[j] -= nums[i]
            
            memo[(i, hashkey)] = res

            return res
        
        cur = [0] * k
        return backtrack(0, cur)
