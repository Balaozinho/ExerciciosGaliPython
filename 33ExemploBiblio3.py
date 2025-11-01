import pygame

pygame.init()
tela = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Movendo um círculo 🟢")

x, y = 200, 150
velocidade = 5
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    tela.fill((255, 255, 255))
    pygame.draw.circle(tela, (0, 255, 0), (x, y), 20)
    pygame.display.update()

pygame.quit()
