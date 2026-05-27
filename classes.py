import pygame
pygame.init()

#I dont know how to add custom fonts

def get_image(sheet, xframe, yframe, width, height, scale, color):
    image = pygame.Surface((width, height))
    image.blit(sheet, (0, 0), ((xframe * width), (yframe * height), width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)
    return image

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
class Tile:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.Surface((tileSize, tileSize))
        self.image.fill((255, 0, 255))
        self.image = get_image(image, x, y, tileSize, tileSize, 1, (90, 0, 0))

    def draw(self, screen):
        self.image.blit(screen, (self.x, self.y))
        #need image to draw

    def update(self, screen):
        self.draw(screen)