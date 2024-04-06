import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colisión y Movimiento de Sprite")

# Definir colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clase de Sprite
class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

# Crear sprite
sprite = MySprite(100, 100, 50, 50)

# Velocidad de movimiento del sprite
SPEED = 1

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener el estado del teclado
    keys = pygame.key.get_pressed()

    # Mover el sprite según las teclas presionadas
    if keys[pygame.K_LEFT]:
        sprite.move(-SPEED, 0)
    if keys[pygame.K_RIGHT]:
        sprite.move(SPEED, 0)
    if keys[pygame.K_UP]:
        sprite.move(0, -SPEED)
    if keys[pygame.K_DOWN]:
        sprite.move(0, SPEED)

    # Limpiar la pantalla
    WINDOW.fill(WHITE)

    # Dibujar sprite
    pygame.draw.rect(WINDOW, RED, sprite.rect)

    # Detectar colisión con los bordes de la ventana
    if sprite.rect.left < 0 or sprite.rect.right > WIDTH or sprite.rect.top < 0 or sprite.rect.bottom > HEIGHT:
        pygame.draw.rect(WINDOW, GREEN, sprite.rect, 5)
        print(f"colision : {sprite.rect}")

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
