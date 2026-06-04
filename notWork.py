from classes import *
import random

pygame.init()

running = True; clock = pygame.time.Clock()
win = pygame.display.set_mode((1000, 700))

player = Player()

tiles = []

for j in range(22):
    row = []
    for i in range(18):
        if j == 0 or j == 21 or i == 0 or i == 17:
            row.append(Tile(130+ tileSize*i, 40+ tileSize*j, 'wall'))
        else:
            row.append(Tile(130 + tileSize * i, 40 + tileSize * j, 'bg'))
    tiles.append(row)

test = Text(300, 20, 'This is text', 15, None, (255, 0, 0))

blocks = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'cyan']

for i in range(3):
    player.upNext.append(Block(800, 300-i*90, random.choice(blocks)))

player.blocks.append(Block(130+tileSize*2, 40+tileSize*2, random.choice(blocks)))
block = player.blocks[-1]
block.selected = True

while running:
    if block.stationary:
        player.blocks.append(Block(130 + tileSize * 2, 40 + tileSize * 2, player.upNext[-1].type))
        block = player.blocks[-1]
        block.selected = True
        player.upNext.pop(-1)
        for block in player.upNext:
            block.y -= 90
        player.upNext.append(Block(800, 300-3*90, random.choice(blocks)))
    block.update(win)
    block.move(block.x, block.y, tiles, player)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    test.draw(win)
    for row in tiles:
        for tile in row:
            tile.update(win)

    for block in player.upNext:
        block.update(win)

    for block in player.blocks:
        block.update(win)

    pygame.draw.line(win, (140, 140, 140), (400, 20 * tileSize + 70), (400, 70 ), 3)

    pygame.display.flip()
    win.fill((255, 255, 255))
    clock.tick(60)

pygame.quit()