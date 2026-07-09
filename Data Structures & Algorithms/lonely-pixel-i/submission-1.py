class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows = [0] * len(picture)
        cols = [0] * len(picture[0])

        for i, row in enumerate(picture):
            if "B" in row:
                rows[i] += row.count("B")
        
        for j in range(len(picture[0])):
            for i in range(len(picture)):
                if picture[i][j] == "B":
                    cols[j] += 1
        
        res = 0
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == "B" and rows[i] == 1 and cols[j] == 1:
                    res += 1
        
        return res

