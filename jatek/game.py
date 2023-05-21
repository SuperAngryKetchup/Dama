import pygame
from .constants import RED, WHITE, BLUE, SQUARE_SIZE, pcwins, playerwins, player1wins, player2wins
from jatek.board import Board


# ez a class vezérli a játékot
class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        """
        frissíti a táblát
        """
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def winner(self):
        """
        visszaadja a nyertest, ha van
        """
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        """
        kiválasztja a tábla egy adott mezőjén lévő elemet
        """
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False

    def _move(self, row, col):
        """
        ha van valami kiválasztva, azt átmozgatja a megadott helyre
        """
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True
    
    def check_for_draw(self):
        """
        ellenőrzi, hogy van-e olyan játékos aki nem tud lépni. Ez az AI elleni játékban használt változat.
        """
        pieces = self.board.get_all_pieces(self.turn)
        possible_moves = []
        for piece in pieces:
            possible_moves.append(self.board.get_valid_moves(piece))

        if not any(possible_moves):
            ext = True
            if self.turn==WHITE:
                while ext:
                    self.win.blit(playerwins,(0,0))
                    pygame.display.update()
                    for ev in pygame.event.get():
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            ext=False
            if self.turn==RED:
                while ext:
                    self.win.blit(pcwins,(0,0))
                    pygame.display.update()
                    for ev in pygame.event.get():
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            ext=False
            pygame.quit()
            exec(open('ezt_inditsd.py', "rb").read(), globals())
            exit()
    
    def check_for_draw_2(self):
        """
        ellenőrzi, hogy van-e olyan játékos aki nem tud lépni. Ez az 2 játékos játékban használt változat.
        """
        pieces = self.board.get_all_pieces(self.turn)
        possible_moves = []
        for piece in pieces:
            possible_moves.append(self.board.get_valid_moves(piece))

        if not any(possible_moves):
            ext = True
            if self.turn==WHITE:
                while ext:
                    self.win.blit(player1wins,(0,0))
                    pygame.display.update()
                    for ev in pygame.event.get():
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            ext=False
            if self.turn==RED:
                while ext:
                    self.win.blit(player2wins,(0,0))
                    pygame.display.update()
                    for ev in pygame.event.get():
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            ext=False
            print(f"The game ended in a draw because {self.turn} has no moves left.")
            pygame.quit()
            exec(open('ezt_inditsd.py', "rb").read(), globals())
            exit()

    def draw_valid_moves(self, moves):
        """
        Kirajzolja a lehetséges lépéseket a kiválasztott bábuhoz.
        """
        if self.selected:
            for move in moves:
                row, col = move
                pygame.draw.rect(self.win, BLUE, (col *SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                #pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)
        if self.selected and moves:
            pygame.draw.rect(self.win, BLUE, (self.selected.col *SQUARE_SIZE, self.selected.row *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            self.selected.draw(self.win)

    def change_turn(self):
        """
        Átadja a kört a másik játékosnak.
        """
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()