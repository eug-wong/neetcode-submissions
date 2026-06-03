class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # o(n^2) just test it, two pointer
        # use set to keep track of window of size k
        
        l, r = 0, 0
        s = set()
        while r < len(nums):
            while r < len(nums) and r - l <= k:
                if nums[r] in s:
                    return True
                s.add(nums[r])
                r += 1
            s.clear()
            l += 1
            r = l

        return False
