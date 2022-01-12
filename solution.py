import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Жёлтый круг')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)

    running = True
    fps = 100
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                d = True
                pos = event.pos
                r = 0
        screen.fill((0, 0, 255))
        if d:
            r = r + 1
            pygame.draw.circle(screen, (255, 255, 0), (pos), r)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
