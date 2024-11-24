import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Game settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape the Abandoned Mansion")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)  # Color for walls/structures

# Player settings
player_width = 50
player_height = 50
player_speed = 5
player_pos = [screen_width // 2, screen_height // 2]
player_direction = 0  # Angle in radians, initially facing right
player_health = 100

# Bullet settings
bullet_width = 3
bullet_height = 10
bullet_speed = 7
bullets = []

# Zombie settings
zombie_width = 50
zombie_height = 50
zombie_speed = 1
zombies = []

# Wall settings
walls = []

# Score
score = 0

# Font for text
font = pygame.font.SysFont(None, 30)

# Clock to control the game speed
clock = pygame.time.Clock()

# Player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = player_width
        self.height = player_height
        self.speed = player_speed
        self.health = player_health

    def move(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed
        
        # Prevent the player from going out of bounds
        if self.x < 0:
            self.x = 0
        if self.x > screen_width - self.width:
            self.x = screen_width - self.width
        if self.y < 0:
            self.y = 0
        if self.y > screen_height - self.height:
            self.y = screen_height - self.height

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

    def lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            return True  # Game over
        return False

# Bullet class
class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.width = bullet_width
        self.height = bullet_height
        self.speed = bullet_speed
        self.direction = direction  # -1 for left, 1 for right

    def move(self):
        self.x += self.direction * self.speed

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

# Zombie class
class Zombie:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = zombie_width
        self.height = zombie_height
        self.speed = zombie_speed
    
    def move(self, player_x, player_y):
        # Move towards the player
        dx = player_x - self.x
        dy = player_y - self.y
        dist = math.sqrt(dx**2 + dy**2)
        
        if dist != 0:
            dx /= dist
            dy /= dist
        
        self.x += dx * self.speed
        self.y += dy * self.speed
    
    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

# Wall class
class Wall:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(screen, BROWN, (self.x, self.y, self.width, self.height))

# Function to spawn zombies randomly
def spawn_zombie():
    x = random.randint(0, screen_width - zombie_width)
    y = random.randint(0, screen_height - zombie_height)
    return Zombie(x, y)

# Function to spawn walls randomly
def spawn_wall():
    width = random.randint(50, 150)
    height = random.randint(50, 150)
    x = random.randint(0, screen_width - width)
    y = random.randint(0, screen_height - height)
    return Wall(x, y, width, height)

# Function to check collision between two objects
def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

# Function to display the health bar
def draw_health_bar(health):
    pygame.draw.rect(screen, WHITE, (10, 10, 200, 20))
    pygame.draw.rect(screen, RED, (10, 10, health * 2, 20))

# Function to display the score
def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 40))

# Function to display Game Over screen
def game_over():
    game_over_text = font.render("GAME OVER", True, WHITE)
    retry_text = font.render("Press R to Retry", True, WHITE)
    screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 50))
    screen.blit(retry_text, (screen_width // 2 - 100, screen_height // 2))

# Main game loop
def game_loop():
    global score
    global player_health
    running = True
    player = Player(screen_width // 2, screen_height // 2)
    zombies = [spawn_zombie() for _ in range(5)]  # Start with 5 zombies
    walls = [spawn_wall() for _ in range(3)]  # Add some random walls
    bullets = []
    global score
    global player_health

    while running:
        screen.fill(BLACK)
        keys = pygame.key.get_pressed()
        
        # Handle player movement
        player.move(keys)
        
        # Shooting bullets
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Shoot bullet in the direction the player is facing
                    bullets.append(Bullet(player.x + player.width // 2, player.y, 1))
        
        # Move bullets and check for collisions
        for bullet in bullets[:]:
            bullet.move()
            if bullet.x > screen_width:  # Remove bullet if it goes out of bounds
                bullets.remove(bullet)
            for zombie in zombies[:]:
                if check_collision(pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height),
                                   pygame.Rect(zombie.x, zombie.y, zombie.width, zombie.height)):
                    bullets.remove(bullet)
                    zombies.remove(zombie)
                    zombies.append(spawn_zombie())  # Spawn a new zombie
                    score += 1  # Increase score

        # Move zombies and check for collision with player
        for zombie in zombies:
            zombie.move(player.x, player.y)
            if check_collision(pygame.Rect(player.x, player.y, player.width, player.height),
                               pygame.Rect(zombie.x, zombie.y, zombie.width, zombie.height)):
                # Player touches zombie, lose health
                if player.lose_health(25):
                    running = False  # Game over
                zombies.remove(zombie)
                zombies.append(spawn_zombie())  # Spawn a new zombie
        
        # Draw everything
        player.draw()
        for bullet in bullets:
            bullet.draw()
        for zombie in zombies:
            zombie.draw()
        for wall in walls:
            wall.draw()

        # Draw health bar, score
        draw_health_bar(player.health)
        draw_score()
        
        # Check if game is over
        if player.health <= 0:
            game_over()
            pygame.display.update()
            running = False

        pygame.display.update()
        clock.tick(60)

# Start the game loop
while True:
    game_loop()
    # Wait for the player to press R to restart
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Restart the game
                    score = 0
                    player_health = 100
                    waiting_for_input = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

# Quit Pygame
pygame.quit()
