class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        highest = 0
        res = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > highest:
                res.append(i)
            highest = max(highest, heights[i])
        
        return res[::-1]