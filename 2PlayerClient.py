from twoPlayerClasses import *
import random

pygame.init()

running = True; clock = pygame.time.Clock()
win = pygame.display.set_mode((1000, 700))

player = Player()

for j in range(22):
    row = []
    for i in range(18):
        if j == 0 or j == 21 or i == 0 or i == 17:
            row.append(Tile(130+ tileSize*i, 40+ tileSize*j, j, 'wall'))
        else:
            row.append(Tile(130 + tileSize * i, 40 + tileSize * j, j, 'bg'))
    player.tiles.append(row)

for j in range(12):
    row = []
    for i in range(8):
        if j == 0 or j == 11 or i == 0 or i == 7:
            row.append(Tile(130 + tileSize * (i + 20), 40 + tileSize * (j + 5), j, 'wall'))
        else:
            row.append(Tile(130 + tileSize * (i + 20), 40 + tileSize * (j + 5), j, 'bg'))
    player.nextTiles.append(row)

scoreText = Text(775, 80, 50, None, (0,0,0))
upNextText = Text(755, 130, 70, None, (0,0,0))

blocks = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'cyan']
# blocks = ['red']

for i in range(3):
    player.upNext.append(Block(130 + tileSize * 23, (40 + tileSize * 14)-i*tileSize * 3, random.choice(blocks),1))

player.blocks.append(Block(130 + tileSize * 10, 40+tileSize*2, random.choice(blocks),1))
block1 = player.blocks[-1]
block1.selected = True
player.blocks.append(Block(130 + tileSize * 2, 40+tileSize*2, random.choice(blocks),2))
block2 = player.blocks[-1]
block2.selected = True

while running:
    if block1.stationary:
        player.blocks.append(Block(130 + tileSize * 10, 40 + tileSize, player.upNext[-1].type, 1))
        block1 = player.blocks[-1]
        block1.selected = True
        player.upNext.pop(-1)
        for block in player.upNext:
            for tile in block.blocks:
                tile.y -= tileSize * 3
        player.upNext.insert(0, Block(130 + tileSize * 23, (40 + tileSize * 14), random.choice(blocks),1))
    if block2.stationary:
        player.blocks.append(Block(130 + tileSize * 2, 40 + tileSize, player.upNext[-1].type, 2))
        block2 = player.blocks[-1]
        block2.selected = True
        player.upNext.pop(-1)
        for block in player.upNext:
            for tile in block.blocks:
                tile.y -= tileSize * 3
        player.upNext.insert(0, Block(130 + tileSize * 23, (40 + tileSize * 14), random.choice(blocks), 2))
    block1.move(player.tiles, player)
    block2.move(player.tiles, player)

    scoreText.update(win, f'Score: {player.score}')
    upNextText.update(win, f'Up Next')
    for row in player.tiles:
        for tile in row:
            tile.update(win, player.blocks, player.tiles, player)

    for row in player.nextTiles:
        for tile in row:
            tile.draw(win)

    for block in player.upNext:
        block.draw(win)

    for block in player.blocks:
        block.update(win, player.tiles, player)

    pygame.draw.line(win, (140, 140, 140), (400, 20 * tileSize + 70), (400, 70 ), 3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                block1.rotate(player)
            if event.key == pygame.K_w:
                block2.rotate(player)

    pygame.display.flip()
    win.fill((255, 255, 255))
    clock.tick(60)

pygame.quit()