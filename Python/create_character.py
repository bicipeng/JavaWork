#chapter 12 -2 
#init params refers to where we will draw the ship
#get_rect(): to access teh surface's rect attriute 
import pygame

class Mario():
	def __init__(self,screen):
		self.screen = screen

		#load mario and get its rect
		self.image = pygame.image.load('images/mario.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.center = self.screen_rect.center


	def blitme(self):
		'''draw mario at the middle'''
		self.screen.blit(self.image,self.rect)
