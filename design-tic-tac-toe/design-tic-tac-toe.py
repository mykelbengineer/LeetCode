class TicTacToe:
    def __init__(self, n: int):
        self.n=n
        self.horiz=[0]*n
        self.vert=[0]*n
        self.diag1=0
        self.diag2=0

    def move(self, row: int, col: int, player: int) -> int:
        n=self.n
        move=1
        if player == 2:
            move=-1
        
        self.horiz[col] += move
        self.vert[row] += move
        
        if row==col: 
            self.diag1 += move
        if row+col == (n-1):
            self.diag2 += move
            
        if abs(self.horiz[col])==n or abs(self.vert[row])==n or abs(self.diag1)==n or abs(self.diag2)==n:
            return player
        return 0