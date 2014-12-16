import pygame
from pygame.locals import *

class Player(object):

	def __init__(self, posX, posY):
		self.x = posX
		self.y = posY
		self.HP = 5

	def render(self, surface):
		pygame.draw.circle(surface, pygame.Color('white'), (self.x, self.y), 10, 0)

	def move_left(self):
		self.x -= 10

	def move_right(self):
		self.x += 10

	def shoot(self):
		pass

class Laser(object):

	def __init__(self, posX, posY):
		self.x = posX
		self.y = posY

	def render(self,surface):
		pygame.draw.circle(surface, pygame.Color('green'), (self.x, self.y), 10, 0)

class Enemy(object):

	def __init__(self, posX, posY):
		self.x = posX
		self.y = posY

	def render(self, surface):
		pygame.draw.circle(surface, pygame.Color('red'), (self.x, self.y), 10, 0)