class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = zip(position, speed)
        sorted_combined = sorted(combined)
        position, speed = zip(*sorted_combined)
        position = position[::-1]
        speed = speed[::-1]

        stack = []
        for i in range(len(position)):
            p, s = position[i], speed[i]
            if not stack:
                stack.append((target - p) / s)
            elif stack[-1] < (target - p) / s:
                stack.append((target - p) / s)
        
        return len(stack)