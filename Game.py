import sys 
import pygame


# FPS = 10>60        # число кадров в секунду
clock = pygame.time.Clock()

X = 0
Y = 0
height = 616
width = 796
size = 15

pygame.init()
screen = pygame.display.set_mode((width, height))
white = (255,255,255)
black = (0,0,0)
purple = (125,50,150)
background = pygame.Surface((width,height))
surface = pygame.Surface((size-1,size-1))
surface_cell = pygame.Surface((size-1,size-1))

surface_cell.fill(white)
surface.fill(black)
background.fill(purple)

pos = [1, 1]
count = 0
grid = []
for x in range(int((height-1)/size)):
    grid += [[[pos.copy(),0,count]]]
    for i in range(int((width-1)/size)-1):
        pos[0] += size
        grid[x] += [[pos.copy(),0,count]]
    pos[0] = 1
    pos[1] += size

run_g = False
while True:

    if run_g:
        for l in range(len(grid)):
            for c in range(len(grid[l])):
                if grid[l][c][1] == 1:
                    grid[l][c-1][2] += 1
                    try:
                        grid[l][c+1][2] += 1
                    except IndexError:
                        grid[l][(c+1)*(-1)][2] += 1


                    grid[l-1][c][2] += 1
                    grid[l-1][c-1][2] += 1
                    try:
                        grid[l-1][c+1][2] += 1
                    except IndexError:
                        grid[l-1][(c+1)*(-1)][2] += 1


                    try:
                        grid[l+1][c][2] += 1
                    except IndexError:
                        grid[(l+1)*(-1)][c][2] += 1
                    try:
                        grid[l+1][c-1][2] += 1
                    except IndexError:
                        grid[(l+1)*(-1)][c-1][2] += 1
                    try:
                        grid[l+1][c+1][2] += 1
                    except IndexError:
                        try:
                            grid[(l+1)*(-1)][c+1][2] += 1
                        except IndexError:
                            try:
                                grid[l+1][(c+1)*(-1)][2] += 1
                            except IndexError:
                                grid[(l+1)*(-1)][(c+1)*(-1)][2] += 1

        for l in grid:
            for c in l:
                if c[1] == 0:
                    if c[2] == 3:
                        c[1] = 1
                    else:
                        c[1] = 0
                else:
                    if c[2] == 3 or  c[2] == 2:
                        c[1] = 1
                    else:
                        c[1] = 0
                c[2] = 0


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            col = int(event.pos[0] / size)
            if col >= int(width/size):
                col -= 1

            line = int(event.pos[1] / size)
            if line >= int(height/size):
                line -= 1
            if grid[line][col][1] == 1:
                grid[line][col][1] = 0
            else:
                grid[line][col][1] = 1
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if run_g == False:
                    run_g = True
                else:
                    run_g = False
                


    screen.blit(background, (0,0))
    for l in grid:
        for c in l:
            if c[1] == 0:
                screen.blit(surface, c[0])
            else:
                screen.blit(surface_cell, c[0])
    
    pygame.display.update()

    clock.tick(10)
