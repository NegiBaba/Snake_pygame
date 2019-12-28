import pygame
pygame.init()

def Grid(surface, rows, side):

	cellSize = side // rows
	for i in range(0, side, cellSize):
		pygame.draw.line(surface, (255, 255, 255), (i, 0), (i, side))
		pygame.draw.line(surface, (255, 255, 255), (0, i), (side, i))

def move(dx, dy, x, y, dis):


	if dx == 1:
		x += dis
	elif dx == -1:
		x -= dis

	if dy == -1:
		y -= dis
	elif dy == 1:
		y += dis

	return x, y

def main():

	clock = pygame.time.Clock()

	rows = 20
	side = 500

	win = pygame.display.set_mode((500, 500))
	pygame.display.set_caption("Grid")


	run = True
	x = 50
	y = 50
	vel = 1
	dis = side // rows
	dx = 1
	dy = 0

	while run:
		pygame.time.delay(100)
		clock.tick(10)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT]:
			dx = -1
			dy = 0
		elif keys[pygame.K_RIGHT]:
			dx = 1
			dy = 0
		elif keys[pygame.K_UP]:
			dx = 0
			dy = -1
		elif keys[pygame.K_DOWN]:
			dx = 0
			dy = 1

		x, y = move(dx, dy, x, y, dis)


		# for box getting out of the borders
		if x > side - dis:
			x = 0
		elif x < 0:
			x = side - dis

		if y > side - dis:
			y = 0
		elif y < 0:
			y = side - dis


		win.fill(((0, 0, 0)))
		Grid(win, rows, side)
		pygame.draw.rect(win, (255, 0, 0), (x + 1, y + 1, dis - 1, dis - 1))
		pygame.display.update()

	pygame.quit()

main()