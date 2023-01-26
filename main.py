import pygame, sys
from pygame.locals import QUIT
from cube import Cube

pygame.init()


screen = pygame.display.set_mode((500, 600))
background = pygame.Surface(screen.get_size())
pygame.Surface.fill(background, (34,34,34))
pygame.display.set_caption('gravity test')
clock = pygame.time.Clock()

gravity = 1
velocity_y = 0
velocity_x = 0
groundLevel = screen.get_size()[1] - 96
dragging = False
x = 50
y = 50
cube = Cube()

def drawBackground():
	screen.blit(background, (0,0))

def calculateVelocity(groundlevel, velocity_y, y, increment):
	aircheck = True
	if y<groundlevel:
		aircheck = True
	if y < groundlevel and dragging == False:
		velocity_y += increment
	elif y >= groundlevel:
		velocity_y = 0
		aircheck=False
	return velocity_y, aircheck

#def collisionChecks(x,y, cube, velocity_x, velocity_y):
	#if x >= screen.get_size()[0] - cube.size[0]:
	#	velocity_x += .6
	#	velocity_y += .5
	#elif not x >= screen.get_size()[0] - cube.size()[0] and velocity_x > 0 or velocity_y > 0:
	#	velocity_x = 0
	#	velocity_y = 0
	#return velocity_x,velocity_y



while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_f:
				cube.explode(screen)


	if pygame.mouse.get_pressed()[0]:
		if cube.rect.collidepoint(pygame.mouse.get_pos()):
			dragging = True
			x = pygame.mouse.get_pos()[0] - 8
			y = pygame.mouse.get_pos()[1] - 8
	if dragging == True and not pygame.mouse.get_pressed()[0]:
		dragging = False

	drawBackground()
	cube.draw(screen,x,y)
	pygame.draw.rect(screen, (19,19,19), pygame.Rect(0,groundLevel+cube.rect.size[0], screen.get_width(), 80))
	velocity_y, aircheck = calculateVelocity(groundLevel, velocity_y,y, .1)
	#velocity_x, velocity_y = collisionChecks(x,y,cube, velocity_x, velocity_y)
	y += velocity_y
	#x -= velocity_x
	if not aircheck and not dragging and y < groundLevel or y>groundLevel:
		y = groundLevel
	pygame.display.update()
	clock.tick(60)