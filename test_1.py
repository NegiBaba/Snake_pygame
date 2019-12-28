import pygame
import os
import random
pygame.init()

WIN_WIDTH = 600
WIND_HEIGHT = 600

SNAKE_HEAD = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "snake1.png")), (40, 40))
HEAD = pygame.image.load(os.path.join("imgs", "Head.png"))
BODY = pygame.image.load(os.path.join("imgs", "Body.png"))
TAIL = pygame.image.load(os.path.join("imgs", "Tail.png"))

win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")
win.fill(((255, 255, 255)))
sh = pygame.transform.rotate(SNAKE_HEAD, -90)
#win.blit(sh, (40, 40))
win.blit(HEAD, (40, 40))
win.blit(BODY, (40, 60))
win.blit(TAIL, (40, 80))

run = True
angle = -90
x = 40
y = 40
vel = 0.1

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		x -= vel
		angle = 90
	if keys[pygame.K_RIGHT]:
		x += vel
		angle = -90
	if keys[pygame.K_UP]:
		y -= vel
		angle = 0
	if keys[pygame.K_DOWN]:
		y += vel
		angle = 180

	if x < -20:
		x = 600
	if x > 600:
		x = -20


	#win.fill(((255, 255, 255)))
	#sh = pygame.transform.rotate(SNAKE_HEAD, angle)
	#win.blit(sh, (x, y))
	pygame.display.update()

pygame.quit()