import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Caja de Colisión")

# Definir colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class MySprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # Reducir el tamaño de la caja de colisión
        self.collision_rect = pygame.Rect(self.rect.x + 30, self.rect.y + 20, self.rect.width - 70, self.rect.height - 35)

    def update(self):
        pass

    def draw_collision_box(self, surface):
        pygame.draw.rect(surface, RED, self.collision_rect, 2)  # Dibujar rectángulo de colisión

# Crear sprite con imagen transparente
sprite = MySprite("transparent_sprite.png", 100, 100)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla
    WINDOW.fill(WHITE)

    # Dibujar sprite y su caja de colisión
    WINDOW.blit(sprite.image, sprite.rect.topleft)
    sprite.draw_collision_box(WINDOW)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
