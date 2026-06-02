from classes import *
import random
#
pygame.init()

running = True; clock = pygame.time.Clock()
win = pygame.display.set_mode((800, 700))

player = Player()

tiles = []

for j in range(22):
    row = []
    for i in range(14):
        if j == 0 or j == 21 or i == 0 or i == 13:
            row.append(Tile(190 + tileSize*i, 40 + tileSize*j, 'wall'))
        else:
            row.append(Tile(190 + tileSize * i, 40 + tileSize * j, 'bg'))
    tiles.append(row)

test = Text(300, 20, 'This is text', 15, None, (255, 0, 0))

blocks = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'cyan']

for i in range(3):
    player.futureBlocks.append(Block(680, 100+i*90, random.choice(blocks)))

player.blocks.append(Block(190+tileSize*2, 40+tileSize*2, player.futureBlocks[0].type))
player.blocks.append(Block(190+tileSize*2, 400+tileSize*2, player.futureBlocks[1].type))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    test.draw(win)
    for row in tiles:
        for tile in row:
            tile.update(win)

    for block in player.blocks:
        block.update(win, tiles, player)

    pygame.draw.line(win, (140, 140, 140), (400, 40 + 20 * tileSize), (400, 70), 3)

    pygame.display.flip()
    win.fill((255, 255, 255))
    clock.tick(60)
pygame.quit()