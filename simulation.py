import pygame
from urdfpy import URDF
from collections.abc import Mapping


# Inicializar o Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("URDF Robot in Pygame")

# Carregar o URDF
robot = URDF.load("drone.urdf")

# Definir cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Função para desenhar o robô
def draw_robot():
    screen.fill(WHITE)
    for link in robot.links:
        # Exemplo: Desenhar links como círculos (ajuste conforme necessário)
        pygame.draw.circle(screen, BLUE, (400, 300), 20)
    pygame.display.flip()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_robot()

pygame.quit()
