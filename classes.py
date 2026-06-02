import pygame
pygame.init()

class Player:
    def __init__(self):
        self.score = 0
        self.futureBlocks = []
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
#
    def top_collisions(self, player):
        for block in player.blocks:
            for image in block.blocks:
                if image.x >= self.x+1 >= image.x + tileSize and self.y + tileSize * 1.2 >= image.y and not image:
                    return True
                if
        return False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Block:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.speed = 25
        self.tick = 0

        self.blocks = []
        if self.type == 'red':
            self.add(Image(x, y, 'redTile.png'))
            self.add(Image(x, y - tileSize, 'redTile.png'))
            self.add(Image(x + tileSize, y - tileSize, 'redTile.png'))
            self.add(Image(x - tileSize, y, 'redTile.png'))
        elif self.type == 'blue':
            self.add(Image(x, y, 'blueTile.png'))
            self.add(Image(x - tileSize, y, 'blueTile.png'))
            self.add(Image(x + tileSize, y, 'blueTile.png'))
            self.add(Image(x - tileSize, y - tileSize, 'blueTile.png'))
        elif self.type == 'green':
            self.add(Image(x, y, 'greenTile.png'))
            self.add(Image(x, y - tileSize, 'greenTile.png'))
            self.add(Image(x - tileSize, y - tileSize, 'greenTile.png'))
            self.add(Image(x + tileSize, y, 'greenTile.png'))
        elif self.type == 'yellow':
            self.add(Image(x, y, 'yellowTile.png'))
            self.add(Image(x, y - tileSize, 'yellowTile.png'))
            self.add(Image(x + tileSize, y - tileSize, 'yellowTile.png'))
            self.add(Image(x + tileSize, y, 'yellowTile.png'))
        elif self.type == 'orange':
            self.add(Image(x, y, 'orangeTile.png'))
            self.add(Image(x - tileSize, y, 'orangeTile.png'))
            self.add(Image(x + tileSize, y, 'orangeTile.png'))
            self.add(Image(x + tileSize, y - tileSize, 'orangeTile.png'))
        elif self.type == 'purple':
            self.add(Image(x, y, 'purpleTile.png'))
            self.add(Image(x - tileSize, y, 'purpleTile.png'))
            self.add(Image(x + tileSize, y, 'purpleTile.png'))
            self.add(Image(x, y - tileSize, 'purpleTile.png'))
        elif self.type == 'cyan':
            self.add(Image(x,y, 'cyanTile.png'))
            self.add(Image(x - tileSize, y, 'cyanTile.png'))
            self.add(Image(x + tileSize, y, 'cyanTile.png'))
            self.add(Image(x + tileSize * 2, y, 'cyanTile.png'))
    def add(self, image):
        self.blocks.append(image)

    def move(self, x, y, tiles, player):
        keys = pygame.key.get_pressed()
        for block in self.blocks:
            if self.tick % self.speed == 0:
                if not block.top_collisions(player):
                    block.y += tileSize

            # if keys[pygame.K_DOWN] and not block.top_collisions(tiles):
            #     block.speed = 5
            # else:
            #     block.speed = 25
            # if keys[pygame.K_RIGHT] and not block.right_collisions(tiles):
            #     block.x += tileSize
            # if keys[pygame.K_LEFT] and not block.left_collisions(tiles):
            #     block.x -= tileSize


    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)

    def right_collisions(self, tiles):
        for block in self.blocks:
            for tile in tiles[self.row]:
                if block.x + tileSize >= 550 and tile.type == 'wall':
                    return True
        return False

    def left_collisions(self, tiles):
        for block in self.blocks:
            for tile in tiles[self.row]:
                if block.x <= 250 and tile.type == 'wall':
                    return True
        return False

    def update(self, screen, tiles, player):

        self.move(screen, self.x, tiles, player)
        self.draw(screen)
        self.tick += 1

tileSize = 30
class Tile:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.size = tileSize
        self.type = type

        if type == 'bg':
            self.image = pygame.image.load('bgTile.png')
            self.image = pygame.transform.scale(self.image, (tileSize, tileSize))

        elif type == 'wall':
            self.image = pygame.image.load('wallTile.png')
            self.image = pygame.transform.scale(self.image, (tileSize, tileSize))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, screen):
        self.draw(screen)