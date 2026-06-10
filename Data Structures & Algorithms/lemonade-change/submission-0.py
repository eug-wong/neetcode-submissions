class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bank = defaultdict(int)
        for bill in bills:
            bank[bill] += 1

            change = bill - 5
            for k in [20, 10, 5]:
                while bank[k] > 0 and change - k >= 0:
                    change -= k
                    bank[k] -= 1
            
            if change != 0:
                return False
        
        return True