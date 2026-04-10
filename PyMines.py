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
    x = 0
    y = 0
    searched = False
    hovered = False
    selected = False
    bomb = False
    image = block_img
    image_selected = block_img_selected

    def __init__(self, pos):
        self.pos = pos

    def set_alpha_on(self):
        self.image_selected.set_alpha(2)
        draw_grid.blit(cell.image_selected, ((start_x + (l * spr_x)), start_y + (r * spr_y)))
    
    def __str__(self):
        return f"Selected: {self.selected} \nBombs: {self.bomb} \nSource Images: {self.image}, {self.image_selected} \nPosition: {self.pos}"

#Initialization

around = [
    (-1, 0), # Esquerda
    (-1, -1), # Esquerda Cima
    (0, -1), # Cima
    (1, -1), # Direita Cima
    (1, 0), # Direita
    (1, 1), # Direita Baixo
    (0, 1), # Baixo
    (-1, 1), # Esquerda Baixo
]

dir = len(around)

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
ra = (1, 1)

for l in range(height):
    for r in range(width): 
        grid[l][r] = Cell((l, r))
        grid[l][r].x = l
        grid[l][r].y = r
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
            hover = mouse[0] > (start_x + (l * spr_x)) and mouse[0] < ((start_x + (l * spr_x)) + block_img.get_width()) and mouse[1] > (start_y + (r * spr_y)) and mouse[1] < ((start_y + (r * spr_y)) + block_img.get_height())
            cell = grid[l][r]
            if hover:
                cell.hovered = True
                #print(l, r)
                
                if pygame.mouse.get_pressed()[0] == True and clicou == False: 
                    if cell.bomb == True: 
                        if can_time == False:
                            time = 2000
                            actual_time = pygame.time.get_ticks()
                            can_time = True

                    clicou = True
                    cell.selected = True
                    print(grid[l][r])

                elif pygame.mouse.get_pressed()[0] == False:
                    clicou = False
            else:
                cell.hovered = False
            if cell.hovered == True:
                for a in range(dir):
                    xx = cell.x + around[a][0]
                    yy = cell.y + around[a][1]
                    if xx >= 0 and xx <= 9 and yy >= 0 and yy <= 9:
                        if not grid[xx][yy].bomb == True:
                            continue
                        print(grid[xx][yy])
                        #cell.set_alpha_on()
                        grid[xx][yy].searched = True
                        draw_grid.blit(cell.image_selected, ((start_x + (xx * spr_x)), start_y + (yy * spr_y)))
                cell.set_alpha_on()
                #draw_grid.blit(cell.image_selected, ((start_x + (l * spr_x)), start_y + (r * spr_y)))
            elif cell.hovered == False:
                if cell.searched == False:
                    draw_grid.blit(block_img, ((start_x + (l * spr_x)), start_y + (r * spr_y)))
            cell.searched = False
    
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
