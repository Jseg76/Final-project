from classes import *

pygame.init()

running = True; clock = pygame.time.Clock()
win = pygame.display.set_mode((800, 700))

tiles = pygame.sprite.Group()
for j in range(20):
    row = []
    for i in range(10):
        row.append(Tile(tileSize * i + 250, tileSize * j + 70,
                        '/Users/levikerr/PycharmProjects/Final-projecttrdf/backgroundtile.png'))
    tiles.add(row)

test = Text(300, 20, 'This is text', 15, '/Users/levikerr/PycharmProjects/Final-projecttrdf/PressStart2P.ttf',
            (255, 0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    test.draw(win)
    # tiles.draw(win)
    for row in tiles:
        for tile in row:
            tile.draw(win)
    print(tiles)

    pygame.display.flip()
    win.fill((255, 255, 255))
    clock.tick(60)
pygame.quit()