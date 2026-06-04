class CountSquares:

    def __init__(self):
        self.matrix = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.matrix[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        total = 0
        x1, y1 = point
        for y2 in self.matrix[x1]:
            side = y2 - y1
            if side == 0:
                continue
            
            x3, x4 = x1 + side, x1 - side
            total += self.matrix[x1][y2] * self.matrix[x3][y1] * self.matrix[x3][y2]
            total += self.matrix[x1][y2] * self.matrix[x4][y1] * self.matrix[x4][y2]
        return total
