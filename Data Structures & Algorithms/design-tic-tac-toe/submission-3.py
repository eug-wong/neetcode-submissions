class TicTacToe:

    def __init__(self, n: int):
        self.dim = n
        self.x_rows = defaultdict(int)
        self.o_rows = defaultdict(int)
        self.x_verts = defaultdict(int)
        self.o_verts = defaultdict(int)
        # key = 0 is up diag, key = 1 is down diag
        self.diag_o = defaultdict(int)
        self.diag_x = defaultdict(int)
        self.diags_1 = [(x, y) for (x, y) in zip(range(0, self.dim), range(0, self.dim))]
        self.diags_2 = []
        x, y = self.dim - 1, 0
        for _ in range(self.dim):
            self.diags_2.append((x, y))
            x -= 1
            y += 1

    def move(self, row: int, col: int, player: int) -> int:
        # assume player 1 is o and player 2 is x
        if player == 1:
            self.o_rows[row] += 1
            self.o_verts[col] += 1
            if (row, col) in self.diags_2:
                self.diag_o[0] += 1
                
            if (row, col) in self.diags_1:
                self.diag_o[1] += 1
            
            if self.dim in self.o_rows.values():
                return 1
            
            if self.dim in self.o_verts.values():
                return 1
            
            if self.dim in self.diag_o.values():
                return 1
        else:
            self.x_rows[row] += 1
            self.x_verts[col] += 1
            if (row, col) in self.diags_2:
                self.diag_x[0] += 1

            if (row, col) in self.diags_1:
                self.diag_x[1] += 1
            
            if self.dim in self.x_rows.values():
                return 2
            
            if self.dim in self.x_verts.values():
                return 2
            
            if self.dim in self.diag_x.values():
                return 2
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
