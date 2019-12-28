import pygame
import random
pygame.init()
class cube:

	side = 500
	rows = 20
	def __init__(self, start):
		self.pos = start
		self.dx = 1
		self.dy = 0

	def move(self, dx, dy):
		self.dx = dx
		self.dy = dy
		self.pos = (self.pos[0] + self.dx, self.pos[1] + self.dy)

	def draw(self, surface):
		dis = 500 // 20
		i = self.pos[0]
		j = self.pos[1]

		pygame.draw.rect(surface, (255, 255, 255), (i, j, dis - 2, dis - 2))

class snake():
	body = []

	def __init__(self, pos):
		self.head = cube(pos)
		self.body.append(self.head)
		self.dx = 0
		self.dy = 1

	def move(self):
		keys = pygame.key.get_pressed()

		for key in keys:
			if keys[pygame.K_LEFT]:
				self.dx = -1
				self.dy = 0
			elif keys[pygame.K_RIGHT]:
				self.dx = 1
				self.dy = 0
			elif keys[pygame.K_UP]:
				self.dx = 0
				self.dy = -1
			elif keys[pygame.K_DOWN]:
				self.dx = 0
				self.dy = 1

		for i, c in enumerate(self.body):
			c.move(c.dx, c.dy)

	def draw(self, surface):
		for i, c in enumerate(self.body):
			c.draw(surface)

def drawGrid(side, rows, surface):
	dis = side // rows
	x = 0
	y = 0
	for l in range(rows):
		x += dis
		y += dis
		
		pygame.draw.line(surface, (254, 254, 254), (x, 0), (x, side))
		pygame.draw.line(surface, (254, 254, 254), (0, y), (side, y))

def redrawWindow(surface):
	global rows, side, s
	surface.fill((0, 0, 0))
	s.draw(surface)
	drawGrid(side, rows, surface)
	pygame.display.update()

def main():
	global side, rows, s
	rows = 20
	side = 500
	win = pygame.display.set_mode((side, side))
	s = snake((25, 25))

	run = True

	clock = pygame.time.Clock()

	while run:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		pygame.time.delay(50)
		clock.tick(10)
		s.move()

	redrawWindow(win)
	

main()