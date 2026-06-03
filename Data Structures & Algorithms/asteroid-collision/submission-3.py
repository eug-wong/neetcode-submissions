class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            size = abs(a)

            while stack and stack[-1] > 0 and a < 0 and size != 0:
                if size == abs(stack[-1]):
                    stack.pop()
                    size = 0
                elif size > abs(stack[-1]):
                    stack.pop()
                else:
                    size = 0
            
            if size:
                stack.append(a)
        
        return stack