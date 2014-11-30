import pygame
from pygame.locals import *
from gamelib import SimpleGame
from elements import *
import random

class SpaceFight(SimpleGame):
	BLACK = pygame.Color('black')
	WHITE = pygame.Color('white')
	RED = pygame.Color('red')

	def __init__(self):        
		super(SpaceFight, self).__init__('SpaceFight', SpaceFight.BLACK)
		self.player = Player(posX=390, posY=580)
		self.isShoot = False
		self.enemy = []
		self.gameLevel = 10
		for i in range(self.gameLevel):
			tmp_enemy = Enemy(posX=random.randint(50, 750), posY=100)
			self.enemy.append(tmp_enemy)

	def update(self):
		if self.isShoot:
			self.laser.y -= 10
			print(self.laser.y)
			if(self.laser.y < 0):
				self.isShoot = False

		if self.is_key_pressed(K_SPACE):
			if(self.isShoot == False):
				self.isShoot = True
				self.player.shoot()
				self.laser = Laser(self.player.x, self.player.y)
		elif self.is_key_pressed(K_LEFT):
			self.player.move_left()
		elif self.is_key_pressed(K_RIGHT):
			self.player.move_right()

	def render(self, surface):
		self.player.render(surface)

		for i in range(self.gameLevel):
			self.enemy[i].render(surface)
		if self.isShoot:
			self.laser.render(surface)

	def checkCollision():
		pass


def main():
	game = SpaceFight()
	game.run()

if __name__ == '__main__':
	main()