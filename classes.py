import pygame
pygame.init()

class Player:
    def __init__(self):
        self.score = 0
        self.blocks = []

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

class Image:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (tileSize, tileSize))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Block:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.speed = 5
        self.blocks = []

        if self.type == 'red':
            self.image = Image(x, y, 'redTile.png')
        elif self.type == 'blue':
            ...
        elif self.type == 'green':
            ...
        elif self.type == 'yellow':
            ...
        elif self.type == 'orange':
            ...
        elif self.type == 'pink':
            ...
        elif self.type == 'cyan':
            ...

        self.blocks.append(self.image)

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.x -= 0
        elif key[pygame.K_RIGHT]:
            self.x += 0
        if key[pygame.K_DOWN]:
            self.y += 0

    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)

    def update(self, screen):
        self.draw(screen)

tileSize = 30
class Tile:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.size = tileSize

        if type == 'bg':
            self.image = pygame.image.load('bgTile.png')
            self.image = pygame.transform.scale(self.image, (tileSize, tileSize))

        elif type == 'wall':
            ...

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, screen):
        self.draw(screen)