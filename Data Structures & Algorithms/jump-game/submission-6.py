class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = 0
        for i, num in enumerate(nums):
            if i > can_reach:
                return False
            
            can_reach = max(can_reach, i + num)
        
        return True