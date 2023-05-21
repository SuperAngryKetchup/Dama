import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE
from .piece import Piece

"""
ez a class vezérli a táblát
"""

class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    

    def create_board(self):
        """
        elkészíti a tábla objektumot
        """        
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    
    def draw_squares(self, win):
        """
        megrajzolja a négyzeteket a táblára
        """
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw(self, win):
        """
        megrajzolja a táblát, tehát a négyzeteket és a bábúkat is
        """
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
    
    def get_piece(self, row, col):
        """
        Ezzel a paranccsal kérhetünk le egy bábút adott mezőről
        """
        return self.board[row][col]
        
    def get_all_pieces(self, color):
        """
        Lekérhetjük az összes bábút egy adott színből
        """
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        """
        Egy adott bábút átléptet egy megadott helyre
        """
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE and not piece.king:
                self.white_kings += 1
                piece.make_king()
            if piece.color == RED and not piece.king:
                self.red_kings += 1
                piece.make_king()
                
    def evaluate(self):
        """
        kiértékeli a táblát. Azaz megad egy számot, hogy a játék ezen állapota mennyire értékes A CPU-nak
        """
        return self.white_left - 2*self.red_left + (self.white_kings * 0.03 - self.red_kings * 0.05)

    
    def remove(self, pieces):
        """
        Kitörli az adott bábút
        """
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1
    
    def winner(self):
        """
        Ha valaki megnyerte a játékot, azt adja vissza ez a függvény
        """
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED
        
        return None 
    
    def get_valid_moves(self, piece):
        """
        Megadja egy bábú lehetséges lépéseit
        """
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._left_search(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._right_search(row -1, max(row-3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._left_search(row +1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._right_search(row +1, min(row+3, ROWS), 1, piece.color, right))
    
        return moves

    def _left_search(self, start, stop, step, color, left, skipped=[]):
        """
        Segédfüggvény a get_valid_moves-hoz. Ez egy balra lehetséges lépést keres
        """
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, -1)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._left_search(r+step, row, step, color, left-1,skipped=last))
                    moves.update(self._right_search(r+step, row, step, color, left+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    def _right_search(self, start, stop, step, color, right, skipped=[]):
        """
        Segédfüggvény a get_valid_moves-hoz. Ez egy jobbra lehetséges lépést keres
        """
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, -1)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._left_search(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self._right_search(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves