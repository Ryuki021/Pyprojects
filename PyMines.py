import pygame

pygame.init()

### Create Event ###

grid = []
width = 10
height = 10

for lines in range(height):
    lines = []
    for rows in range(width):
        lines.append(0)
    grid.append(lines)

screen = pygame.display.set_mode((640, 640))
block_img = pygame.image.load('spr-box.png').convert_alpha()

draw_grid = pygame.Surface((640, 640), pygame.SRCALPHA)

start_x = screen.get_width() / 2 - (((block_img.get_width() + 10) * width) / 2)
start_y = screen.get_height() / 2 - (((block_img.get_height() + 10) * height + 10) / 2)

spr_x = block_img.get_width()
spr_y = block_img.get_height()

for l in range(height):
    for r in range(width): 
        draw_grid.blit(block_img, (start_x + (l * spr_x), start_y + (r * spr_y)))

clock = pygame.time.Clock()
running = True

delta_time = 0
x = 0

#print(grid)

for l in range(height):
        for r in range(width): 
            print(((start_x + (l * spr_x)), (start_y + (r * spr_y))))

### Step Event ###

while (running):
    screen.fill((0, 65, 78))
    screen.blit(draw_grid, (0, 0))

    mouse = pygame.mouse.get_pos()

    for l in range(height):
        for r in range(width): 
            #print(((start_x + (l * spr_x)), (start_y + (r * spr_y))))
            if mouse[0] > (start_x + (l * spr_x)) and mouse[0] < ((start_x + (l * spr_x)) + spr_x) and mouse[1] > (start_y + (r * spr_y)) and mouse[1] < ((start_y + (r * spr_y)) + spr_y):
                print(mouse)
            
    

    '''
    screen.blit(potatoes, (x, 30))
    x += 10 * delta_time
    '''

    for event in pygame.event.get():
        #print(event)

        if event.type != pygame.QUIT: continue
        running = False
    
    pygame.display.flip()

    delta_time = clock.tick(60) / 1000

pygame.quit()
