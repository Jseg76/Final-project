from classes import *

pygame.init()

running = True; clock = pygame.time.Clock()
win = pygame.display.set_mode((800, 700))

player = Player()

tiles = []

for j in range(20):
    row = []
    for i in range(12):
        row.append(Tile(tileSize * i + 250, tileSize * j + 70, 'bg'))
    tiles.append(row)

test = Text(300, 20, 'This is text', 15, None, (255, 0, 0))

blocks = ['red', 'blue', 'green', 'yellow', 'orange', 'pink', 'cyan']
#        2*2off   L        2*2off   square      L        T     1*4
player.blocks.append(Block(50, 100, 'red'))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    test.draw(win)
    for row in tiles:
        for tile in row:
            tile.update(win)

    for block in player.blocks:
        block.update(win)

    pygame.display.flip()
    win.fill((255, 255, 255))
    clock.tick(60)
pygame.quit()