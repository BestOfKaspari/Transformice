import pygame

pygame.init()

# Define game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5

# Load game assets
standing_image = pygame.image.load("standing.png")
moving_image = pygame.image.load("moving.png")
ground_image = pygame.image.load("ground.png")

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def handle_input(player_rect):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= PLAYER_SPEED
        return "moving"
    if keys[pygame.K_RIGHT]:
        player_rect.x += PLAYER_SPEED
        return "moving"
    if keys[pygame.K_UP]:
        player_rect.y -= PLAYER_SPEED
        return "moving"
    if keys[pygame.K_DOWN]:
        player_rect.y += PLAYER_SPEED
        return "moving"
    return "standing"

def update_player_position(player_rect, ground_rect):
    if player_rect.colliderect(ground_rect):
        player_rect.bottom = ground_rect.top

def update_screen(screen, player_rect, ground_rect, image):
    screen.blit(ground_image, ground_rect)
    screen.blit(image, player_rect)
    pygame.display.update()

def main():
    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Game")

    # Set up the game objects
    player_rect = standing_image.get_rect()
    player_rect.x = SCREEN_WIDTH // 2
    player_rect.y = SCREEN_HEIGHT // 2
    image = standing_image

    ground_rect = ground_image.get_rect()
    ground_rect.y = SCREEN_HEIGHT - ground_rect.height

    # Start the game loop
    while True:
        handle_events()

        image = standing_image
        image_playing = handle_input(player_rect)

        if image_playing == "moving":
            image = moving_image

        update_player_position(player_rect, ground_rect)

        update_screen(screen, player_rect, ground_rect, image)

if __name__ == "__main__":
    main()
