from classes import *
import pygame

pygame.init()

running = True; clock = pygame.time.Clock()
win = pygame.display.set_mode((800, 700))

tiles = []
for j in range(20):
    row = []
    for i in range(10):
        row.append(Tile(tileSize*i+250, tileSize*j+70))
    tiles.append(row)


test = Text(300, 10, 'This is text', 50, None, (255, 0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    test.draw(win)
    for row in tiles:
        for tile in row:
            tile.draw(win)
    print(tiles)

    pygame.display.flip()
    win.fill((255, 255, 255))
    clock.tick(60)
pygame.quit()