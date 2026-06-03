class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        forward = [0] * len(heights)
        # forward pass
        for i, h in enumerate(heights):
            if not stack:
                stack.append([h, i])
                continue
            
            while stack and stack[-1][0] > h:
                popped = stack.pop()
                forward[popped[1]] = i - popped[1]
                
            stack.append([h, i])
        
        while stack:
            popped = stack.pop()
            forward[popped[1]] = len(heights) - popped[1]
 
        # backwards
        stack = []
        backward = [0] * len(heights)
        for i in range(len(heights) - 1, -1, -1):
            h = heights[i]
            if not stack:
                stack.append([h, i])
                continue
            
            while stack and stack[-1][0] > h:
                popped = stack.pop()
                backward[popped[1]] = popped[1] - i
            
            stack.append([h, i])
        
        while stack:
            popped = stack.pop()
            backward[popped[1]] = popped[1] + 1
        
        maximum = 0
        for h, l, r in zip(heights, backward, forward):
            maximum = max(maximum, h * (r + l - 1))


        return maximum