import pygame
import random

pygame.init()

# Define game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
ROOMS = ["Room 1", "Room 2", "Room 3", "Room 4", "Room 5"]

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

def change_room():
    if random.randint(0, 1000) < 5:
        return random.choice(ROOMS)
    return None

def draw_objects(screen, current_room, player_rect, image, ground_rect):
    screen.fill((255, 255, 255))
    screen.blit(image, player_rect)

    # Draw the ground
    for i in range(0, SCREEN_WIDTH, ground_image.get_width()):
        for j in range(0, SCREEN_HEIGHT, ground_image.get_height()):
            screen.blit(ground_image, (i, j))

    # Draw the camera view
    camera_rect = pygame.Rect(player_rect.x - SCREEN_WIDTH // 2, player_rect.y - SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT)
    camera_ground_rect = pygame.Rect(player_rect.x - SCREEN_WIDTH // 2, SCREEN_HEIGHT - ground_image.get_height(), SCREEN_WIDTH, ground_image.get_height())
    pygame.draw.rect(screen, (255, 0, 0), camera_rect, 2)
    pygame.draw.rect(screen, (0, 255, 0), camera_ground_rect, 2)

def main():
    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Game")

    # Set up the game objects
    player_rect = standing_image.get_rect()
    player_rect.x = SCREEN_WIDTH // 2
    player_rect.y = SCREEN_HEIGHT // 2
    image = standing_image
    image_playing = "standing"
    current_room = random.choice(ROOMS)

    # Start the game loop
    while True:
        handle_events()

        image_playing = handle_input(player_rect)

        if image_playing == "moving":
            image = moving_image
        else:
            image = standing_image

        new_room = change_room()
        if new_room:
            current_room = new_room

        draw_objects(screen, current_room, player_rect, image, ground_image.get_rect())

        pygame.display.update()

if __name__ == "__main__":
    main()
