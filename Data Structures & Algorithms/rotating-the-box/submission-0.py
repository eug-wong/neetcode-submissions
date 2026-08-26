class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows, cols = len(boxGrid), len(boxGrid[0])
        rotated = [[boxGrid[rows-1-j][i] for j in range(rows)] for i in range(cols)]

        rows, cols = len(rotated), len(rotated[0])
        for col in range(cols):
            l, r = rows - 1, rows - 1
            while r >= 0:
                if rotated[r][col] == "*":
                    l = r - 1
                elif rotated[r][col] == "#":
                    rotated[l][col], rotated[r][col] = rotated[r][col], rotated[l][col]
                    l -= 1
                
                r -= 1
        
        return rotated