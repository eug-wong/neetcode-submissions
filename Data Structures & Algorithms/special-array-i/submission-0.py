class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        parity = nums[0] % 2
        for num in nums[1: ]:
            if parity and num % 2 == 1:
                return False
            elif not parity and num % 2 == 0:
                return False
            
            parity = num % 2
        
        return True