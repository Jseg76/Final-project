from classes import *
import random

pygame.init()

running = True; clock = pygame.time.Clock()
win = pygame.display.set_mode((800, 700))

player = Player()

tiles = []

for j in range(20):
    row = []
    for i in range(12):
        row.append(Tile(220+tileSize*i, 70+tileSize*j, 'bg'))
    tiles.append(row)

test = Text(300, 20, 'This is text', 15, None, (255, 0, 0))

blocks = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'cyan']

for i in range(3):
    player.blocks.append(Block(680, 100+i*90, random.choice(blocks)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    test.draw(win)
    for row in tiles:
        for tile in row:
            tile.update(win)

    pygame.draw.line(win, (140, 140, 140), (400, 70+20*tileSize), (400, 70), 3)
    pygame.draw.rect(win, (140, 140, 140), (220, 70, 12*tileSize, 20*tileSize), 4)

    for block in player.blocks:
        block.update(win)

    pygame.display.flip()
    win.fill((255, 255, 255))
    clock.tick(60)
pygame.quit()