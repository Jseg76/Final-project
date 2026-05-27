import pygame
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
            self.x -= 0
        elif key[pygame.K_RIGHT]:
            self.x += 0
        if key[pygame.K_DOWN]:
            self.y += 0

    def draw(self, screen):
        ...

    def update(self, screen):
        self.draw(screen)

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
        self.x = x
        self.y = y
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, scale)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def collide(self):
        ...

    def update(self, screen):
        self.draw(screen)