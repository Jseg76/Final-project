import pygame
from pygame import surface

pygame.init()

#I dont know how to add custom fonts

class Text:
    def __init__(self, x, y, text, size, font, color):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.size = size
        self.color = color

    def draw(self, screen):
        font = pygame.font.Font(self.font, self.size)
        text = font.render(self.text, True, self.color)
        screen.blit(text, (self.x, self.y))

    def update(self, screen):
        self.draw(screen)

class Block:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.speed = 5

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.x -= 1
        elif key[pygame.K_RIGHT]:
            self.x += 1
        if key[pygame.K_DOWN]:
            self.y += 1

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), (self.x, self.y, self, self.speed))

    def update(self, screen):
        self.draw(screen)
        self.move()

tileSize = 30
class BackgroundTile:
    def __init__(self, x, y, image, scale):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, scale)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, screen):
        self.draw(screen)

class WallTile:
    def __init__(self, x, y, image, scale):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, scale)
        self.x, self.y = x, y
        self.left, self.right = x, x + self.image.get_width()
        self.top, self.bottom = y, y + self.image.get_height()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def collide(self):
        ...

    def update(self, screen):
        self.draw(screen)