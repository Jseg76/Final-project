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
    def __init__(self, x, y, size, font, color):
        self.x = x
        self.y = y
        self.text = None
        self.font = font
        self.size = size
        self.color = color

    def draw(self, screen):
        font = pygame.font.Font(self.font, self.size)
        text = font.render(self.text, True, self.color)
        screen.blit(text, (self.x, self.y))

    def update(self, screen, text):
        self.text = text
        self.draw(screen)

class Image:
    def __init__(self, x, y, image, type):
        self.x = x
        self.y = y
        self.type = type
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (tileSize, tileSize))

    def collide(self, x, y, other):
        if other.x <= x+5 <= other.x+tileSize and other.y <= y+5 <= other.y+tileSize:
            return True
        return False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def rotate(self, x, y, tiles):
        dx = self.x - x
        dy = self.y - y
        for row in tiles:
            for tile in row:
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
            self.add(Image(x, y, 'redTile.png', self.type))
            self.add(Image(x, y-tileSize, 'redTile.png', self.type))
            self.add(Image(x+tileSize, y-tileSize, 'redTile.png', self.type))
            self.add(Image(x-tileSize, y, 'redTile.png', self.type))
        elif self.type == 'blue':
            self.add(Image(x, y, 'blueTile.png', self.type))
            self.add(Image(x-tileSize, y, 'blueTile.png', self.type))
            self.add(Image(x+tileSize, y, 'blueTile.png', self.type))
            self.add(Image(x-tileSize, y-tileSize, 'blueTile.png', self.type))
        elif self.type == 'green':
            self.add(Image(x, y, 'greenTile.png', self.type))
            self.add(Image(x, y-tileSize, 'greenTile.png', self.type))
            self.add(Image(x-tileSize, y-tileSize, 'greenTile.png', self.type))
            self.add(Image(x+tileSize, y, 'greenTile.png', self.type))
        elif self.type == 'yellow':
            self.add(Image(x, y, 'yellowTile.png', self.type))
            self.add(Image(x, y-tileSize, 'yellowTile.png', self.type))
            self.add(Image(x+tileSize, y-tileSize, 'yellowTile.png', self.type))
            self.add(Image(x+tileSize, y, 'yellowTile.png', self.type))
        elif self.type == 'orange':
            self.add(Image(x, y, 'orangeTile.png', self.type))
            self.add(Image(x-tileSize, y, 'orangeTile.png', self.type))
            self.add(Image(x+tileSize, y, 'orangeTile.png', self.type))
            self.add(Image(x+tileSize, y-tileSize, 'orangeTile.png', self.type))
        elif self.type == 'purple':
            self.add(Image(x, y, 'purpleTile.png', self.type))
            self.add(Image(x-tileSize, y, 'purpleTile.png', self.type))
            self.add(Image(x+tileSize, y, 'purpleTile.png', self.type))
            self.add(Image(x, y-tileSize, 'purpleTile.png', self.type))
        elif self.type == 'cyan':
            self.add(Image(x, y, 'cyanTile.png', self.type))
            self.add(Image(x-tileSize, y, 'cyanTile.png', self.type))
            self.add(Image(x+tileSize, y, 'cyanTile.png', self.type))
            self.add(Image(x+tileSize*2, y, 'cyanTile.png', self.type))

    def add(self, image):
        self.blocks.append(image)

    def move(self, tiles, player):
        keys = pygame.key.get_pressed()
        if self.aTick < 5:
            self.aTick += 1

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

    def testCollisions(self, player):
        for block in self.blocks:
            if block.x == 640 or block.x == 130 or block.y == 670:
                return True
            else:
                for pBlock in player.blocks:
                    for tile in pBlock.blocks:
                        if tile.x == block.x and tile.y == block.y and not tile in self.blocks:
                            return True
        return False

    def rotate(self, player):
        if not self.type == 'yellow':
            for image in self.blocks:
                image.rotate(self.x, self.y, player.tiles)
            if self.testCollisions(player):
                print(player.tiles[-1][1].y)
                for i in range(3):
                    for image in self.blocks:
                        image.rotate(self.x, self.y, player.tiles)

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
                    if block.y + tileSize == tile.y and not tile in self.blocks:
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
                    if block.x + tileSize >= tile.x > block.x and not tile in self.blocks:
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
                    if tile.x + tileSize >= block.x > tile.x and not tile in self.blocks:
                        if block.y == tile.y:
                            return True
        return False

    def update(self, screen, tiles, player):
        self.draw(screen)
        if self.tick % self.speed == 0:
            if not self.top_collisions(tiles, player):
                self.stationary = False
                for block in self.blocks:
                    block.y += tileSize
                self.y += tileSize
                self.row += 1
                if self.speed == 5:
                    player.score += 1
            else:
                self.stationary = True
        self.tick += 1

class Tile:
    def __init__(self, x, y, row, type):
        self.row = row
        self.x = x
        self.y = y
        self.size = tileSize
        self.type = type
        self.cleared = False
        self.occupiedImage = Image(10000, 10000, 'redTile.png', 'nonExistant')
        self.occupied = False

        if type == 'bg':
            self.image = pygame.image.load('bgTile.png')
            self.image = pygame.transform.scale(self.image, (tileSize, tileSize))

        elif type == 'wall':
            self.image = pygame.image.load('wallTile.png')
            self.image = pygame.transform.scale(self.image, (tileSize, tileSize))

    def unoccupy(self, player):
        self.occupied = False
        for block in player.blocks:
            for tile in block.blocks:
                if tile.type == self.occupiedImage.type and tile.x == self.occupiedImage.x and tile.y == self.occupiedImage.y:
                    block.blocks.remove(tile)
        self.cleared = False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, screen, blocks, tiles, player):
        self.draw(screen)
        self.occupied = False
        for block in blocks:
            for image in block.blocks:
                if image.x == self.x and image.y == self.y and block.stationary:
                    self.occupied = True
                    self.occupiedImage = image

        for row in tiles:
            numTilesOcupied = 0
            for tile in row:
                tile.stationary = False
                if tile.occupied:
                    numTilesOcupied += 1
                    tile.cleared = True
            if numTilesOcupied == len(row) - 2:
                for tile in row:
                    if tile.cleared:
                        tile.unoccupy(player)
                player.score += numTilesOcupied*10