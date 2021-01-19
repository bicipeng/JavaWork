#chapter 12 
#12-1 blue sky: make a pygame windwoe with a blue background (204,255,255)
#sys exit the game , pygame functionalities needed to make a game
import pygame
import sys
from create_character import Mario

def open_screen():
	pygame.init()
	screen = pygame.display.set_mode((1200,1000))
	pygame.display.set_caption("Blue Sky")
	bg_color = (204,255,255)

	#make mario
	mario = Mario(screen)
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill(bg_color)
		#draw the character on the screen
		mario.blitme()

		pygame.display.flip()

open_screen()


