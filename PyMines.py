import pygame

pygame.init()

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
#potato_img = pygame.transform.scale(potato_img, (potato_img.get_width() * 2, potato_img.get_height() * 2))

potatoes = pygame.Surface((640, 640), pygame.SRCALPHA)
for l in range(height):
    for r in range(width): 
        potatoes.blit(block_img, (l * block_img.get_width() + 10, r * block_img.get_height() + 10))

clock = pygame.time.Clock()
running = True

delta_time = 0
x = 0

print(grid)

while (running):
    screen.fill((0, 65, 78))
    screen.blit(potatoes, (screen.get_width() / 2 - potatoes.get_width() / 4, screen.get_height() / 2 - potatoes.get_height() / 4))

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
