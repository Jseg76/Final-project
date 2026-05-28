from classes import *

pygame.init()

running = True; clock = pygame.time.Clock()
win = pygame.display.set_mode((800, 700))

player = Player()

tiles = []

for j in range(20):
    row = []
    for i in range(12):
        row.append(BackgroundTile(tileSize * i + 250, tileSize * j + 70,'backgroundtile.png', (tileSize,tileSize)))
    tiles.append(row)

test = Text(300, 20, 'This is text', 15, None, (255, 0, 0))

blocks = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    test.draw(win)
    for row in tiles:
        for tile in row:
            tile.update(win)

    pygame.display.flip()
    win.fill((255, 255, 255))
    clock.tick(60)
pygame.quit()