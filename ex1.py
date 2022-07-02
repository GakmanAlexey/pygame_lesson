import pygame

pygame.init()
pygame.display.set_mode((1280, 720),pygame.OPENGL )
clock = pygame.time.Clock()
pygame.display.set_caption("Навзвания Окна")
pygame.display.set_icon(pygame.image.load("app.png"))
flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False

    clock.tick(60)