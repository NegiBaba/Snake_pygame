import pygame
pygame.init()


def draw(surface, x, y, cellSize):
    pygame.draw.rect(surface, (255, 0, 0), (x + 1, y + 1, cellSize - 1, cellSize - 1))

def grid(Surface, side, rows):
    cellSize = side // rows

    for i in range(0, side, cellSize):
        pygame.draw.line(Surface, (255, 255, 255), (i, 0), (i, side))
        pygame.draw.line(Surface, (255, 255, 255), (0, i), (side, i))

def move(body, dx, dy, dis, surface):

    for i in range(len(body)):
    	x = body[i][0]
    	y = body[i][1]
    	if dx == 1:
    		x += dis
    	elif dx == -1:
    		x -= dis

    	if dy == 1:
    		y += dis
    	elif dy == -1:
    		y -= dis
    	
    	if x < 0:
    		x = 500 - dis
    	elif x > 500 - dis:
    		x = 0
    	if y < 0:
    		y = 500 - dis
    	elif y > 500 - dis:
    		y = 0

    	body[i][0] = x
    	body[i][1] = y

    	draw(surface, x, y, dis)


def main():
    side = 500
    rows = 20
    dx = 1
    dy = 0
    dis = side // rows
    win = pygame.display.set_mode((side, side))
    body = [[0, 0], [25, 0]]
    
    run = True
    while run:
    	pygame.time.delay(100)

    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			run = False

    	win.fill((0,0,0))
    	grid(win, side, rows)
    	move(body, 1, 0, dis, win)
    	pygame.display.update()

    pygame.quit()
main()