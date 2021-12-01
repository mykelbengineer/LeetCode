class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti = 0
        self.size = n   

    def move(self, row: int, col: int, player: int) -> int:
        boardSize = self.size
        
        p_sign = 1
        if player == 2: p_sign = -1
            
        
        self.rows[row] += p_sign
        self.cols[col] += p_sign
        
        if row == col: self.diag += p_sign
        if row + col == boardSize - 1: self.anti += p_sign
            
        if abs(self.rows[row]) == boardSize or abs(self.cols[col]) == boardSize or abs(self.diag) == boardSize or abs(self.anti) == boardSize:
            return player
        
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)