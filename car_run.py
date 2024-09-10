import pygame
import sys

# Inicializa Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movimiento del Carro")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Cargar la imagen del carro
car_image = pygame.image.load("car.png")
car_width, car_height = car_image.get_size()

# Posición inicial del carro
car_x = 0
car_y = (HEIGHT - car_height) // 2

# Velocidad del carro
car_speed = 5

# Fuente para el texto
font = pygame.font.Font(None, 36)

# Opciones de respuesta
options = [
    (1, "3 km/h"),
    (2, "5 km/h"),
    (3, "7 km/h")
]
correct_option = 2

def draw_question_and_options():
    screen.fill(WHITE)  # Fondo blanco
    screen.blit(car_image, (car_x, car_y))  # Dibujar el carro

    # Mostrar la pregunta
    question_text = font.render("¿A qué velocidad va el carro?", True, BLACK)
    screen.blit(question_text, (20, 20))

    # Mostrar las opciones
    for i, (key, option) in enumerate(options):
        option_text = font.render(f"{key}: {option}", True, BLACK)
        screen.blit(option_text, (20, 60 + i * 40))

    pygame.display.flip()

def get_user_input():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        return 1
    elif keys[pygame.K_2]:
        return 2
    elif keys[pygame.K_3]:
        return 3
    return None

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mover el carro
    car_x += car_speed

    # Si el carro sale de la pantalla, reinicia su posición
    if car_x > WIDTH:
        car_x = -car_width

    draw_question_and_options()

    # Obtener la respuesta del usuario
    answer = get_user_input()
    if answer is not None:
        if answer == correct_option:
            print("¡Bien hecho!")
        else:
            print(f"Respuesta correcta: {options[correct_option - 1][1]}")
        pygame.time.wait(2000)  # Pausa para mostrar la respuesta
        car_x = -car_width  # Reinicia la posición del carro para comenzar de nuevo

    # Controlar la velocidad de fotogramas
    pygame.time.Clock().tick(60)
