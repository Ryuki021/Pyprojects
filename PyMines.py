import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))
potato_img = pygame.image.load('spr-box.png').convert()
clock = pygame.time.Clock()
running = True

delta_time = 0
x = 0

while (running):
    screen.fill((0, 65, 78))

    screen.blit(potato_img, (x, 30))
    x += 10 * delta_time

    for event in pygame.event.get():
        #print(event)

        if event.type != pygame.QUIT: continue
        running = False
    
    pygame.display.flip()

    delta_time = clock.tick(60) / 1000

pygame.quit()
