import pygame

pygame.init()

tileSize = 30

class Player:
    def __init__(self):
        self.score = 0
        self.blocks = []
        self.upNext = []
        self.tiles = []

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

    def rotate(self, x, y):
        dx = self.x - x
        dy = self.y - y
        self.x = dy
        self.y = -dx
        self.x += x
        self.y += y

class Block:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.speed = 25
        self.tick = 0
        self.aTick = 0
        self.rTick = 0
        self.row = 2
        self.stationary = False
        self.selected = False
        self.blocks = []
        if self.type == 'red':
            self.add(Image(x, y, 'redTile.png'))
            self.add(Image(x, y-tileSize, 'redTile.png'))
            self.add(Image(x+tileSize, y-tileSize, 'redTile.png'))
            self.add(Image(x-tileSize, y, 'redTile.png'))
        elif self.type == 'blue':
            self.add(Image(x, y, 'blueTile.png'))
            self.add(Image(x-tileSize, y, 'blueTile.png'))
            self.add(Image(x+tileSize, y, 'blueTile.png'))
            self.add(Image(x-tileSize, y-tileSize, 'blueTile.png'))
        elif self.type == 'green':
            self.add(Image(x, y, 'greenTile.png'))
            self.add(Image(x, y-tileSize, 'greenTile.png'))
            self.add(Image(x-tileSize, y-tileSize, 'greenTile.png'))
            self.add(Image(x+tileSize, y, 'greenTile.png'))
        elif self.type == 'yellow':
            self.add(Image(x, y, 'yellowTile.png'))
            self.add(Image(x, y-tileSize, 'yellowTile.png'))
            self.add(Image(x+tileSize, y-tileSize, 'yellowTile.png'))
            self.add(Image(x+tileSize, y, 'yellowTile.png'))
        elif self.type == 'orange':
            self.add(Image(x, y, 'orangeTile.png'))
            self.add(Image(x-tileSize, y, 'orangeTile.png'))
            self.add(Image(x+tileSize, y, 'orangeTile.png'))
            self.add(Image(x+tileSize, y-tileSize, 'orangeTile.png'))
        elif self.type == 'purple':
            self.add(Image(x, y, 'purpleTile.png'))
            self.add(Image(x-tileSize, y, 'purpleTile.png'))
            self.add(Image(x+tileSize, y, 'purpleTile.png'))
            self.add(Image(x, y-tileSize, 'purpleTile.png'))
        elif self.type == 'cyan':
            self.add(Image(x, y, 'cyanTile.png'))
            self.add(Image(x-tileSize, y, 'cyanTile.png'))
            self.add(Image(x+tileSize, y, 'cyanTile.png'))
            self.add(Image(x+tileSize*2, y, 'cyanTile.png'))

    def add(self, image):
        self.blocks.append(image)

    def move(self, x, y, tiles, player):
        if self.tick % self.speed == 0:
            if not self.top_collisions(tiles, player):
                for block in self.blocks:
                    block.y += tileSize
                self.y += tileSize
                self.row += 1
            else:
                self.stationary = True
                self.selected = False
        keys = pygame.key.get_pressed()
        if self.aTick < 5:
            self.aTick += 1
        if self.rTick < 50:
            self.rTick += 1

        if keys[pygame.K_DOWN] and not self.top_collisions(tiles, player) and not self.stationary:
            self.speed = 5
        else:
            self.speed = 25
        if keys[pygame.K_RIGHT] and not self.right_collisions(tiles, player) and not self.stationary:
            if self.aTick % 5 == 0:
                for block in self.blocks:
                    block.x += tileSize
                self.x += tileSize
                self.aTick = 0
        if keys[pygame.K_LEFT] and not self.left_collisions(tiles, player) and not self.stationary:
            if self.aTick % 5 == 0:
                for block in self.blocks:
                    block.x -= tileSize
                self.x -= tileSize
                self.aTick = 0

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.type != 'yellow':
                    for block in self.blocks:
                        block.rotate(self.x, self.y)
                        self.rTick = 0

    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)

    def top_collisions(self, tiles, player):
        for block in self.blocks:
            for tile in tiles[-1]:
                if block.y + tileSize >= tile.y and tile.type == 'wall':
                    return True
            for pBlock in player.blocks:
                for tile in pBlock.blocks:
                    if block.y + tileSize == tile.y and not pBlock.selected:
                        if block.x < tile.x + tileSize and block.x + tileSize > tile.x:
                            return True
        return False

    def right_collisions(self, tiles, player):
        for block in self.blocks:
            for tile in tiles[self.row]:
                if block.x + tileSize >= 630 and tile.type == 'wall':
                    return True
            for pBlock in player.blocks:
                for tile in pBlock.blocks:
                    if block.x + tileSize >= tile.x > block.x and not pBlock.selected:
                        if block.y == tile.y:
                            return True

        return False

    def left_collisions(self, tiles, player):
        for block in self.blocks:
            for tile in tiles[self.row]:
                if block.x <= 160 and tile.type == 'wall':
                    return True
            for pBlock in player.blocks:
                for tile in pBlock.blocks:
                    if tile.x + tileSize >= block.x > tile.x and not pBlock.selected:
                        if block.y == tile.y:
                            return True
        return False

    def update(self, screen):
        self.draw(screen)
        self.tick += 1

class Tile:
    def __init__(self, x, y, row, type):
        self.row = row
        self.x = x
        self.y = y
        self.size = tileSize
        self.type = type
        self.occupiedImage = Image(x, y, 'redTile.png')
        self.occupied = False

        if type == 'bg':
            self.image = pygame.image.load('bgTile.png')
            self.image = pygame.transform.scale(self.image, (tileSize, tileSize))

        elif type == 'wall':
            self.image = pygame.image.load('wallTile.png')
            self.image = pygame.transform.scale(self.image, (tileSize, tileSize))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, screen, blocks, tiles):
        self.draw(screen)
        self.occupied = False
        for block in blocks:
            for image in block.blocks:
                if image.x == self.x and image.y == self.y:
                    self.occupied = True
                    self.occupiedImage = image

        for row in tiles:
            numTilesOcupied = 0
            for tile in row:
                if tile.occupied:
                    numTilesOcupied += 1
            print(numTilesOcupied, len(row))
            if numTilesOcupied == len(row) - 2:
                print('cleared!')
                self.occupiedImage.x = 62789



