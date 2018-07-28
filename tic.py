import pygame,sys

screen = pygame.display.set_mode((512, 512))
pygame.display.set_caption("Tic-Tac-Toe")

cross = pygame.image.load("cross.png")
circle = pygame.image.load("circle.png")
xwin = pygame.image.load("xwin.png")
owin = pygame.image.load("owin.png")
draw = pygame.image.load("draw.png")
gamemode = 1
game = [ 0, 0, 0, 0, 0, 0, 0, 0, 0]
while True:
    pygame.draw.line(screen, (255, 0, 0), [170, 0], [170, 512], 3)
    pygame.draw.line(screen, (255, 0, 0), [340, 0], [340, 512], 3)
    pygame.draw.line(screen, (255, 0, 0), [0, 170], [512, 170], 3)
    pygame.draw.line(screen, (255, 0, 0), [0, 340], [512, 340], 3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if gamemode == 1:
                if pygame.mouse.get_pos()[0] < 170 and pygame.mouse.get_pos()[1] < 170 and game[0] == 0:
                    game[0] = 1
                    screen.blit(cross, (0,0))
                    gamemode = 2
                if 170 < pygame.mouse.get_pos()[0] < 340 and pygame.mouse.get_pos()[1] < 170 and game[1] == 0:
                    game[1] = 1
                    screen.blit(cross, (170,0))
                    gamemode = 2
                if 340 < pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[1] < 170 and game[2] == 0:
                    game[2] = 1
                    screen.blit(cross, (340,0))
                    gamemode = 2
                if pygame.mouse.get_pos()[0] < 170 and 170 < pygame.mouse.get_pos()[1] < 340 and game[3] == 0:
                    game[3] = 1
                    screen.blit(cross, (0,170))
                    gamemode = 2
                if 170 < pygame.mouse.get_pos()[0] < 340 and 170 < pygame.mouse.get_pos()[1] <340 and game[4] == 0:
                    game[4] = 1
                    screen.blit(cross, (170,170))
                    gamemode = 2
                if 340 < pygame.mouse.get_pos()[0] and 170 < pygame.mouse.get_pos()[1] <340 and game[5] == 0:
                    game[5] = 1
                    screen.blit(cross, (340,170))
                    gamemode = 2
                if pygame.mouse.get_pos()[0] < 170 and 340 < pygame.mouse.get_pos()[1] and game[6] == 0:
                    game[6] = 1
                    screen.blit(cross, (0,340))
                    gamemode = 2
                if 170 < pygame.mouse.get_pos()[0] < 340 and 340 < pygame.mouse.get_pos()[1] and game[7] == 0:
                    game[7] = 1
                    screen.blit(cross, (170,340))
                    gamemode = 2
                if 340 < pygame.mouse.get_pos()[0] and 340 < pygame.mouse.get_pos()[1] and game[8] == 0:
                    game[8] = 1
                    screen.blit(cross, (340,340))
                    gamemode = 2
                
            else:
                if pygame.mouse.get_pos()[0] < 170 and pygame.mouse.get_pos()[1] < 170 and game[0] == 0:
                    game[0] = 2
                    screen.blit(circle, (0,0))
                    gamemode = 1
                if 170 < pygame.mouse.get_pos()[0] < 340 and pygame.mouse.get_pos()[1] < 170 and game[1] == 0:
                    game[1] = 2
                    screen.blit(circle, (170,0))
                    gamemode = 1
                if 340 < pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[1] < 170 and game[2] == 0:
                    game[2] = 2
                    screen.blit(circle, (340,0))
                    gamemode = 1
                if pygame.mouse.get_pos()[0] < 170 and 170 < pygame.mouse.get_pos()[1] < 340 and game[3] == 0:
                    game[3] = 2
                    screen.blit(circle, (0,170))
                    gamemode = 1
                if 170 < pygame.mouse.get_pos()[0] < 340 and 170 < pygame.mouse.get_pos()[1] <340 and game[4] == 0:
                    game[4] = 2
                    screen.blit(circle, (170,170))
                    gamemode = 1
                if 340 < pygame.mouse.get_pos()[0] and 170 < pygame.mouse.get_pos()[1] <340 and game[5] == 0:
                    game[5] = 2
                    screen.blit(circle, (340,170))
                    gamemode = 1
                if pygame.mouse.get_pos()[0] < 170 and 340 < pygame.mouse.get_pos()[1] and game[6] == 0:
                    game[6] = 2
                    screen.blit(circle, (0,340))
                    gamemode = 1
                if 170 < pygame.mouse.get_pos()[0] < 340 and 340 < pygame.mouse.get_pos()[1] and game[7] == 0:
                    game[7] = 2
                    screen.blit(circle, (170,340))
                    gamemode = 1
                if 340 < pygame.mouse.get_pos()[0] and 340 < pygame.mouse.get_pos()[1] and game[8] == 0:
                    game[8] = 2
                    screen.blit(circle, (340,340))
                    gamemode = 1
                


    if (game[0] == 1 and game[1] == 1 and game[2] == 1) or (game[3] == 1 and game[4] == 1 and game[5] == 1) or (game[6] == 1 and game[7] == 1 and game[8] == 1) or (game[0] == 1 and game[3] == 1 and game[6] == 1) or (game[1] == 1 and game[4] == 1 and game[7] == 1) or (game[2] == 1 and game[5] == 1 and game[8] == 1) or (game[0] == 1 and game[4] == 1 and game[8] == 1) or (game[2] == 1 and game[4] == 1 and game[6] == 1):
        screen.fill((0,0,0))
        screen.blit(xwin, (0,0))

    elif (game[0] == 2 and game[1] == 2 and game[2] == 2) or (game[3] == 2 and game[4] == 2 and game[5] == 2) or (game[6] == 2 and game[7] == 2 and game[8] == 2) or (game[0] == 2 and game[3] == 2 and game[6] == 2) or (game[1] == 2 and game[4] == 2 and game[7] == 2) or (game[2] == 2 and game[5] == 2 and game[8] == 2) or (game[0] == 2 and game[4] == 2 and game[8] == 2) or (game[2] == 2 and game[4] == 2 and game[6] == 2):
        screen.fill((0,0,0))
        screen.blit(owin, (0,0))

    elif game[0] != 0 and game[1] != 0 and game[2] != 0 and game[3] != 0 and game[4] != 0 and game[5] != 0 and game[6] != 0 and game[7] != 0 and game[8] != 0:
    	screen.fill((0,0,0))
    	screen.blit(draw, (0,0))

    pygame.display.update()