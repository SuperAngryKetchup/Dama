import pygame
import sys
  
  
# initializing the constructor
pygame.init()
  
# screen resolution
res = (800,800)
  
# opens up a window
screen = pygame.display.set_mode(res)
  
# white color
color = (255,255,255)
  
# light shade of the button
color_light = (170,170,170)
  
# dark shade of the button
color_dark = (100,100,100)
  
# stores the width of the
# screen into a variable
width = screen.get_width()
  
# stores the height of the
# screen into a variable
height = screen.get_height()
  
# defining a font
smallfont = pygame.font.SysFont('Corbel',35)
  
# rendering a text written in
# this font
text_AI = smallfont.render('uj jatek AI ellen' , True , color)
text = smallfont.render('uj jatek 2 jatekos' , True , color)
  
while True:
    
    mouse = pygame.mouse.get_pos()
    
    for ev in pygame.event.get():
          
        if ev.type == pygame.QUIT:
            pygame.quit()
              
        #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the
            # button the game is terminated
            if width/2-125 <= mouse[0] <= width/2+125 and height/2-125 <= mouse[1] <= height/2-75:
                #execfile('main.py')
                exec(open('main_1.py', "rb").read(), globals())
                #exec(compile(open('main.py', "rb").read(), 'main.py', 'exec'))
            if width/2-125 <= mouse[0] <= width/2+125 and height/2-25 <= mouse[1] <= height/2+25:
                #execfile('main_2.py')
                exec(open('main_2.py', "rb").read(), globals())
                #exec(compile(open('main_2.py', "rb").read(), 'main_2.py', 'exec'))
                  
    # fills the screen with a color
    screen.fill((60,25,60))
      
      
    # if mouse is hovered on a button it
    # changes to lighter shade 
    if width/2-125 <= mouse[0] <= width/2+125 and height/2-125 <= mouse[1] <= height/2-75:
        pygame.draw.rect(screen,color_light,[width/2-125,height/2-125,250,50])
          
    else:
        pygame.draw.rect(screen,color_dark,[width/2-125,height/2-125,250,50])
        
    if width/2-125 <= mouse[0] <= width/2+125 and height/2-25 <= mouse[1] <= height/2+25:
        pygame.draw.rect(screen,color_light,[width/2-125,height/2-25,250,50])
          
    else:
        pygame.draw.rect(screen,color_dark,[width/2-125,height/2-25,250,50])
      
    # superimposing the text onto our button
    screen.blit(text_AI , (width/2-100,height/2-117))
    screen.blit(text , (width/2-113,height/2-17))
      
    # updates the frames of the game
    pygame.display.update()