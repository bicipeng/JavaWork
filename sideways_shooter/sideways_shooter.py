import sys
import pygame
from settings import Settings

def run_game():
	#Initialize game and create a screen object
	pygame.init()
	#make a screen with spefific size 
	#create an instance of Settings() class
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
	#give the screen a title
	pygame.display.set_caption("Sideways Shooter")

	#start the main loop for the game
	while True:

		#use pygame.event.get() to watch for the keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill(settings.bg_color)
		#make the most recently drawn screen visible
		pygame.display.flip()

run_game()