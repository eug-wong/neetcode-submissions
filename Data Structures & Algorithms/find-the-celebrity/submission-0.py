# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            knowed_by = 0
            for j in range(n):
                if i == j:
                    continue
                
                if knows(i, j):
                    break
                
                if knows(j, i):
                    knowed_by += 1
            
            if knowed_by == n - 1:
                return i
        
        return -1