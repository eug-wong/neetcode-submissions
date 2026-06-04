class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mult = 1
        int_num1 = 0
        for i in range(len(num1) - 1, -1, -1):
            int_num1 += mult * (ord(num1[i]) - 48)
            mult *= 10
        
        mult = 1
        int_num2 = 0
        for i in range(len(num2) - 1, -1, -1):
            int_num2 += mult * (ord(num2[i]) - 48)
            mult *= 10
        
        return str(int_num1 * int_num2)