import pygame
import random
import sys

pygame.init()

# Define game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
ROOMS = ["Room 1", "Room 2", "Room 3", "Room 4", "Room 5"]
PLAYER_STATS = {"cheese": 0, "saved": 0, "shaman_cheese": 0}

# Load game assets
standing_image = pygame.image.load("standing.png")
moving_image = pygame.image.load("moving.png")

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

def update_stats():
    PLAYER_STATS["cheese"] += 1

def draw_objects(screen, current_room, player_rect, image):
    screen.fill((255, 255, 255))
    screen.blit(image, player_rect)

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 200, 100))
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 16)
    cheese_text = font.render(f"Cheese: {PLAYER_STATS['cheese']}", True, (255, 255, 255))
    saved_text = font.render(f"Saved: {PLAYER_STATS['saved']}", True, (255, 255, 255))
    shaman_cheese_text = font.render(f"Shaman Cheese: {PLAYER_STATS['shaman_cheese']}", True, (255, 255, 255))
    room_text = font.render(f"Current room: {current_room}", True, (255, 255, 255))
    screen.blit(cheese_text, (10, 5))
    screen.blit(saved_text, (10, 25))
    screen.blit(shaman_cheese_text, (10, 45))
    screen.blit(room_text, (10, 75))

def apply_gravity(player_rect):
    player_rect.y += 5

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

        update_stats()

        apply_gravity(player_rect)

        draw_objects(screen, current_room, player_rect, image)

        pygame.display.update()

if __name__ == "__main__":
    main()
