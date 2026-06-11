from twoPlayerClasses import *
import random

# this initilizes the pygame module.
pygame.init()

try:
    with open('highScore.txt', 'r') as file:
        highScore = int(file.read())
except:
    highScore = 0


running = True; clock = pygame.time.Clock()
win = pygame.display.set_mode((1000, 700))

lost = False

# this defines the player
player = Player()

#this creates the grid that the blocks fall in.
for j in range(22):
    row = []
    for i in range(18):
        if j == 0 or j == 21 or i == 0 or i == 17:
            row.append(Tile(130+ tileSize*i, 40+ tileSize*j, j, 'wall'))
        else:
            row.append(Tile(130 + tileSize * i, 40 + tileSize * j, j, 'bg'))
    player.tiles.append(row)

#this creates the grid the blocks that are up next are in
for j in range(12):
    row = []
    for i in range(8):
        if j == 0 or j == 11 or i == 0 or i == 7:
            row.append(Tile(130 + tileSize * (i + 20), 40 + tileSize * (j + 5), j, 'wall'))
        else:
            row.append(Tile(130 + tileSize * (i + 20), 40 + tileSize * (j + 5), j, 'bg'))
    player.nextTiles.append(row)

#this defines the text
scoreText = Text(735, 80, 50, None, (0,0,0))
upNextText = Text(735, 130, 70, None, (0,0,0))
loseText = Text(400, 300, 120, None, (20,0,0))
highScoreText = Text(735, 50, 50, None, (0,0,0))

blocks = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'cyan']

for i in range(3):
    player.upNext.append(Block(130 + tileSize * 23, (40 + tileSize * 14)-i*tileSize * 3, random.choice(blocks),1))

#this adds the stating blocks to the screen
player.blocks.append(Block(130 + tileSize * 10, 40+tileSize*2, random.choice(blocks),1))
block1 = player.blocks[-1]
block1.selected = True
player.blocks.append(Block(130 + tileSize * 2, 40+tileSize*2, random.choice(blocks),2))
block2 = player.blocks[-1]
block2.selected = True

#this is the game loop
while running:
    #checks is the current block for each player has fully fallen and then adds another block if it has, assuming the
    #player has not lost yet
    if not lost:
        if block1.stationary:
            if block1.y <= 40+tileSize*2 and block1.stationary:
                lost = True
            player.blocks.append(Block(130 + tileSize * 10, 40 + tileSize, player.upNext[-1].type, 1))
            block1 = player.blocks[-1]
            block1.selected = True
            player.upNext.pop(-1)
            for block in player.upNext:
                for tile in block.blocks:
                    tile.y -= tileSize * 3
            player.upNext.insert(0, Block(130 + tileSize * 23, (40 + tileSize * 14), random.choice(blocks),1))

        if block2.stationary:
            if block2.y <= 40+tileSize*2 and block2.stationary:
                lost = True
            player.blocks.append(Block(130 + tileSize * 2, 40 + tileSize, player.upNext[-1].type, 2))
            block2 = player.blocks[-1]
            block2.selected = True
            player.upNext.pop(-1)
            for block in player.upNext:
                for tile in block.blocks:
                    tile.y -= tileSize * 3
            player.upNext.insert(0, Block(130 + tileSize * 23, (40 + tileSize * 14), random.choice(blocks), 2))

        #this allows the player to move the blocks
        block1.move(player.tiles, player)
        block2.move(player.tiles, player)

    #this draws and updates the text
    scoreText.update(win, f'Score: {player.score}')
    upNextText.update(win, f'Up Next')
    highScoreText.update(win, f'High Score: {highScore}')

    #this updates all the game objects
    for row in player.tiles:
        for tile in row:
            tile.update(win, player.blocks, player.tiles, player)

    for row in player.nextTiles:
        for tile in row:
            tile.draw(win)

    for block in player.upNext:
        block.draw(win)

    for block in player.blocks:
        if not lost:
            block.update(win, player.tiles, player)
        else:
            block.draw(win)

    #this draws the seperating line
    pygame.draw.line(win, (140, 140, 140), (400, 20 * tileSize + 70), (400, 70 ), 3)

    #this is where some of teh game events are, such as rotations
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not lost:
            if event.key == pygame.K_UP:
                block1.rotate(player)
            if event.key == pygame.K_w:
                block2.rotate(player)

    #this shows the losing screen if you lose
    if lost:
        if player.score > highScore:
            with open('highScore.txt', 'w',encoding="utf-8") as file:
                file.write(str(player.score))
        loseText.update(win, 'You lose!')

    #this updates, fills, and sets the FPS of teh game loop
    pygame.display.flip()
    win.fill((255, 255, 255))
    clock.tick(60)

pygame.quit()
