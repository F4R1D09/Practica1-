import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
RED = (255,0,0)
AZUL = (0,0,255)
GREEN = (0,255,0)

# Definir las dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Definir las dimensiones de las paletas
PALETA_ANCHO = 10
PALETA_ALTO = 100

# Definir la velocidad de movimiento de las paletas
VELOCIDAD = 6

# Definir la velocidad de la pelota
VELOCIDAD_PELOTA = 4
VELOCIDAD_MAX = 10

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong")

# Definir funciones para dibujar las paletas y la pelota
def dibujar_paleta(paleta, color):
    pygame.draw.rect(pantalla, color , paleta)

def dibujar_pelota(pelota):
    pygame.draw.rect(pantalla, BLANCO, pelota)

# Definir la función principal del juego
def main():
    # Inicializar las posiciones de las paletas
    paleta1 = pygame.Rect(50, ALTO // 2 - PALETA_ALTO // 2, PALETA_ANCHO, PALETA_ALTO)
    paleta2 = pygame.Rect(ANCHO - 50 - PALETA_ANCHO, ALTO // 2 - PALETA_ALTO // 2, PALETA_ANCHO, PALETA_ALTO)

    # Inicializar la posición de la pelota
    pelota = pygame.Rect(ANCHO // 2 - 15, ALTO // 2 - 15, 15, 15)

    # Inicializar la velocidad de la pelota
    velocidad_pelota_x = random.choice((VELOCIDAD_PELOTA, -VELOCIDAD_PELOTA))
    velocidad_pelota_y = random.choice((VELOCIDAD_PELOTA, -VELOCIDAD_PELOTA))

    # Inicializar la puntuación
    puntuacion1 = 0
    puntuacion2 = 0

    # Inicializar la fuente para mostrar la puntuación
    fuente = pygame.font.Font(None, 36)

    # Ciclo principal del juego
    while True:
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Movimiento de las paletas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] and paleta1.top > 0:
            paleta1.move_ip(0, -VELOCIDAD)
        if teclas[pygame.K_s] and paleta1.bottom < ALTO:
            paleta1.move_ip(0, VELOCIDAD)
        if teclas[pygame.K_UP] and paleta2.top > 0:
            paleta2.move_ip(0, -VELOCIDAD)
        if teclas[pygame.K_DOWN] and paleta2.bottom < ALTO:
            paleta2.move_ip(0, VELOCIDAD)

        # Movimiento de la pelota
        pelota.move_ip(velocidad_pelota_x, velocidad_pelota_y)

        # Colisiones de la pelota con las paletas y los bordes de la pantalla
        if pelota.top <= 0 or pelota.bottom >= ALTO:
            velocidad_pelota_y = -velocidad_pelota_y
        if pelota.colliderect(paleta1) or pelota.colliderect(paleta2):
            velocidad_pelota_x = -velocidad_pelota_x
            velocidad_pelota_x = min(abs(velocidad_pelota_x) + 0.2, VELOCIDAD_MAX) * (1 if velocidad_pelota_x > 0 else -1)
            velocidad_pelota_y = min(abs(velocidad_pelota_y) + 0.2, VELOCIDAD_MAX) * (1 if velocidad_pelota_y > 0 else -1)

        # Verificar si la pelota sale de la pantalla
        if pelota.left <= 0:
            puntuacion2 += 1
            pelota = pygame.Rect(ANCHO // 2 - 15, ALTO // 2 - 15, 15, 15)
            velocidad_pelota_x = random.choice((VELOCIDAD_PELOTA, -VELOCIDAD_PELOTA))
            velocidad_pelota_y = random.choice((VELOCIDAD_PELOTA, -VELOCIDAD_PELOTA))
        elif pelota.right >= ANCHO:
            puntuacion1 += 1
            pelota = pygame.Rect(ANCHO // 2 - 15, ALTO // 2 - 15, 15, 15)
            velocidad_pelota_x = random.choice((VELOCIDAD_PELOTA, -VELOCIDAD_PELOTA))
            velocidad_pelota_y = random.choice((VELOCIDAD_PELOTA, -VELOCIDAD_PELOTA))

        # Limpiar la pantalla
        pantalla.fill(NEGRO)

        # Dibujar las paletas y la pelota
        dibujar_paleta(paleta1, RED)
        dibujar_paleta(paleta2, AZUL)
        dibujar_pelota(pelota)

        # Mostrar la puntuación
        texto_puntuacion = fuente.render(f"{puntuacion1} - {puntuacion2}", True, BLANCO)
        pantalla.blit(texto_puntuacion, (ANCHO // 2 - texto_puntuacion.get_width() // 2, 20))

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad de fotogramas
        pygame.time.Clock().tick(60)

# Ejecutar el juego
if __name__ == "__main__":
    main()
