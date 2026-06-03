class Solution:
    def trap(self, height: List[int]) -> int:
        # prefix
        # suffix
        prefix = []
        highest = 0
        for h in height:
            highest = max(highest, h)
            prefix.append(highest)

        suffix = [0] * len(height)
        highest = 0
        for i in range(len(height) - 1, -1, -1):
            highest = max(highest, height[i])
            suffix[i] = highest
        
        total = 0
        for i in range(len(height)):
            total += min(suffix[i], prefix[i]) - height[i]

        return total