import pygame
from jatek.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, pcwins, playerwins
from jatek.game import Game
from algoritmus.algorithm import minimax

FPS = 60


pygame.init()
music=pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dáma')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    ext = True

    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            if game.winner()==WHITE:
                while ext:
                    WIN.blit(pcwins,(0,0))
                    pygame.display.update()
                    for ev in pygame.event.get():
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            ext=False
            if game.winner()==RED:
                while ext:
                    WIN.blit(playerwins,(0,0))
                    pygame.display.update()
                    for ev in pygame.event.get():
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            ext=False
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        
        if game.winner() == None:
            game.check_for_draw()
        
        game.update()
        
    pygame.quit()
    #execfile('ezt_inditsd.py')
    exec(open('ezt_inditsd.py', "rb").read(), globals())
    #exec(compile(open('ezt_inditsd.py', "rb").read(), 'ezt_inditsd.py', 'exec'))

main()