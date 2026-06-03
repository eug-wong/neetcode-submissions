class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        carryover = 0 
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carryover
            carryover = digits[i] // 10
            digits[i] = digits[i] % 10
        
        return [carryover] + digits if carryover else digits
