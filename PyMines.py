import pygame
import random

pygame.init()

### Create Event ###

delta_time = 0
time = 1
actual_time = 0
current_time = 0
can_time = False

screen = pygame.display.set_mode((640, 640))
block_img = pygame.image.load('spr-box.png').convert_alpha()
block_img_selected = pygame.image.load('spr-box-selected.png').convert_alpha()

#Classes and Defs

class Cell:
    selected = False
    bomb = False
    image = block_img
    image_selected = block_img_selected

    def __init__(self, pos):
        self.pos = pos
    
    def __str__(self):
        return f"Selected: {self.selected} \nBombs: {self.bomb} \nSource Images: {self.image}, {self.image_selected} \nPosition: {self.pos}"

#Initialization

grid = []
width = 10
height = 10

for lines in range(height):
    lines = []
    for rows in range(width):
        lines.append(0)
    grid.append(lines)

draw_grid = pygame.Surface((640, 640), pygame.SRCALPHA)

start_x = screen.get_width() / 2 - (((block_img.get_width() + 10) * width) / 2)
start_y = screen.get_height() / 2 - (((block_img.get_height() + 10) * height + 10) / 2)

spr_x = block_img.get_width()
spr_y = block_img.get_height()

#ra = (random.randrange(0, 10, 1), random.randrange(0, 10, 1))
ra = (0, 0)

for l in range(height):
    for r in range(width): 
        grid[l][r] = Cell((l, r))
        if l == ra[0] and r == ra[1]:
            grid[l][r].bomb = True
        draw_grid.blit(grid[l][r].image, (start_x + (l * spr_x), start_y + (r * spr_y)))

clock = pygame.time.Clock()
running = True

clicou = False
selecionado = False

### Step Event ###

print(ra)

while (running):
    screen.fill((0, 65, 78))
    screen.blit(draw_grid, (0, 0))

    mouse = pygame.mouse.get_pos()

    for l in range(height):
        for r in range(width): 
            if mouse[0] > (start_x + (l * spr_x)) and mouse[0] < ((start_x + (l * spr_x)) + block_img.get_width()) and mouse[1] > (start_y + (r * spr_y)) and mouse[1] < ((start_y + (r * spr_y)) + block_img.get_height()):
                draw_grid.blit(grid[l][r].image_selected, ((start_x + (l * spr_x)), start_y + (r * spr_y)))
                #print(l, r)
                
                if pygame.mouse.get_pressed()[0] == True and clicou == False: 
                    if grid[l][r].bomb == True: 
                        if can_time == False:
                            time = 2000
                            actual_time = pygame.time.get_ticks()
                            can_time = True
                    clicou = True
                    grid[l][r].selected = not grid[l][r].selected
                    print(grid[l][r])
                elif pygame.mouse.get_pressed()[0] == False:
                    clicou = False
            else:
                draw_grid.blit(block_img, ((start_x + (l * spr_x)), start_y + (r * spr_y)))
    if can_time == True:
        current_time = pygame.time.get_ticks()
        #print(current_time - actual_time)
        #print(time
    if current_time - actual_time >= time:
        running = False
    for event in pygame.event.get():
        #print(event)

        if event.type != pygame.QUIT: continue
        running = False
    pygame.display.flip()

    delta_time = clock.tick(60) / 1000
pygame.quit()
