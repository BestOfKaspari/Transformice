import pygame

# Define game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 1
PLAYER_JUMP_POWER = 5
GRAVITY = 0.3
GROUND_HEIGHT = 550

# Load game assets
standing_image = pygame.image.load("standing.png")
moving_image = pygame.image.load("moving.png")

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def handle_input(player_rect, player_y_speed):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_rect.x += PLAYER_SPEED
    if keys[pygame.K_UP] and player_rect.bottom >= GROUND_HEIGHT:
        player_y_speed = -PLAYER_JUMP_POWER
    return player_y_speed

def update_player(player_rect, player_y_speed):
    player_rect.y += player_y_speed
    player_y_speed += GRAVITY
    if player_rect.bottom > GROUND_HEIGHT:
        player_rect.bottom = GROUND_HEIGHT
        player_y_speed = 0
    return player_y_speed

def draw_objects(screen, player_rect, image):
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (0, GROUND_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_HEIGHT))
    screen.blit(image, player_rect)

def main():
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Game")

    # Set up the game objects
    player_rect = standing_image.get_rect()
    player_rect.x = SCREEN_WIDTH // 2
    player_rect.y = SCREEN_HEIGHT // 2
    image = standing_image
    player_y_speed = 0

    # Start the game loop
    while True:
        handle_events()

        player_y_speed = handle_input(player_rect, player_y_speed)
        player_y_speed = update_player(player_rect, player_y_speed)

        if player_y_speed != 0:
            image = moving_image
        else:
            image = standing_image

        draw_objects(screen, player_rect, image)

        pygame.display.update()

if __name__ == "__main__":
    main()