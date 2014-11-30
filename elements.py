import pygame
from pygame.locals import *

class Player(object):

	def __init__(self, posX, posY):
		self.x = posX
		self.y = posY

	def render(self, surface):
		pygame.draw.circle(surface, pygame.Color('white'), (self.x, self.y), 10, 0)

	def move_left(self):
		print "Left"

		self.x -= 5

	def move_right(self):
		print "Right"

		self.x += 5

	def shoot(self):
		pass

class Laser(object):

	def __init__(self, posX, posY):
		self.x = posX
		self.y = posY
		print "Laser"

	def render(self,surface):
		pygame.draw.circle(surface, pygame.Color('green'), (self.x, self.y), 10, 0)
		print "Shoot"

class Enemy(object):

	def __init__(self, posX, posY):
		self.x = posX
		self.y = posY

	def render(self, surface):
		pygame.draw.circle(surface, pygame.Color('red'), (self.x, self.y), 10, 0)