class Solution:
    def addBinary(self, a: str, b: str) -> str:
        total = int(a) + int(b)
        total = str(total)
        carry = 0
        res = ""
        for i in range(len(total) - 1, -1, -1):
            cur = int(total[i]) + carry
            carry = cur // 2
            cur %= 2
            res = res + str(cur)
        
        if carry:
            res = res + str(carry)

        return res[::-1]