class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
    
        while (b & mask) > 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
            
        # If the carry overflows past 32 bits, mask the final sum 'a'
        num_32bit = a & mask
        
        # Handle negative numbers in 32-bit signed integer logic
        # If the 31st bit is 1, the number is negative in two's complement
        if num_32bit > 0x7FFFFFFF:
            return ~(num_32bit ^ mask)
            
        return num_32bit


