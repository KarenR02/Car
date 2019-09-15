import pygame

display_width = 800
display_height = 600
car_width = 89
pygame.init()

black= (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("A racing game")
clock = pygame.time.Clock()

carImg=pygame.image.load('car.png')

def car(x,y):
	gameDisplay.blit(carImg,(x,y))
	
def game_loop ():
	x=(display_width * 0.4)
	y=(display_height * 0.8)
	x_change = 0

	crashed = False

	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0	
			print(event)
		x+=x_change
		gameDisplay.fill(white)
		car(x,y)

		if x>display_width - car_width or x<0:
			crashed = True 
		pygame.display.update()
		clock.tick(60)

pygame.quit()
quit()