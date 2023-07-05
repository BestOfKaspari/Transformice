import pygame
import random

# Window dimensions
WIDTH = 800
HEIGHT = 600

# Mouse dimensions
MOUSE_WIDTH = 40
MOUSE_HEIGHT = 40

# Platform dimensions
PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 20

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

class Mouse:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.has_cheese = False
        self.velocity_y = 0
    
    def move(self, platforms):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.x += 5

        # Apply gravity
        self.velocity_y += 0.5  # Gravity strength
        self.y += self.velocity_y

        # Check for collisions with platforms
        self.handle_collision(platforms)
    
    def jump(self):
        # Apply upward force for a jump
        self.velocity_y = -10  # Jump force
    
    def collect_cheese(self):
        self.has_cheese = True
        print("Cheese collected!")
    
    def handle_collision(self, platforms):
        for platform in platforms:
            if self.y + MOUSE_HEIGHT > platform.y and self.y < platform.y + PLATFORM_HEIGHT:
                if self.x + MOUSE_WIDTH > platform.x and self.x < platform.x + PLATFORM_WIDTH:
                    self.y = platform.y - MOUSE_HEIGHT
                    self.velocity_y = 0

class Platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, screen, offset):
        pygame.draw.rect(screen, BLUE, (self.x - offset[0], self.y - offset[1], PLATFORM_WIDTH, PLATFORM_HEIGHT))

class Game:
    def __init__(self):
        self.mice = []
        self.platforms = [Platform(WIDTH // 2 - PLATFORM_WIDTH // 2, HEIGHT - 100)]
        self.cheese_collected = False
    
    def play(self):
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Transformice Game")

        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        for mouse in self.mice:
                            mouse.jump()

            # Get the position of the player mouse
            player_x = self.mice[0].x
            player_y = self.mice[0].y

            # Calculate the camera offset
            offset_x = player_x - WIDTH // 2
            offset_y = player_y - HEIGHT // 2

            screen.fill(WHITE)

            for mouse in self.mice:
                mouse.move(self.platforms)
                pygame.draw.rect(screen, (0, 0, 0), (mouse.x - offset_x, mouse.y - offset_y, MOUSE_WIDTH, MOUSE_HEIGHT))

                # Display the name above the player
                font = pygame.font.Font(None, 24)
                text = font.render(mouse.name, True, (255, 0, 0))
                text_rect = text.get_rect(center=(mouse.x - offset_x + MOUSE_WIDTH // 2, mouse.y - offset_y - 20))
                screen.blit(text, text_rect)

                if random.random() < 0.01:  # 1% chance of finding cheese
                    mouse.collect_cheese()
                    self.cheese_collected = True
                    break

            for platform in self.platforms:
                platform.draw(screen, (offset_x, offset_y))

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

# Example usage
game = Game()

# Get player name (minimum length of 3 letters, only first letter capitalized)
player_name = input("Enter your name (minimum 3 letters, only first letter capitalized): ")
while len(player_name) < 3 or not player_name[0].isupper() or player_name[1:].isupper():
    print("Name must be at least 3 letters long, with only the first letter capitalized.")
    player_name = input("Enter your name (minimum 3 letters, only first letter capitalized): ")

player_mouse = Mouse(WIDTH // 2, HEIGHT // 2, player_name)
game.mice.append(player_mouse)

game.play()
