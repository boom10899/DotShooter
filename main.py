import pygame
from pygame.locals import *
from gamelib import SimpleGame
from elements import *
import random

class DotShooter(SimpleGame):
	BLACK = pygame.Color('black')
	WHITE = pygame.Color('white')

	def __init__(self):        
		super(DotShooter, self).__init__('DotShotter', DotShooter.BLACK)
		self.player = Player(posX=390, posY=580)
		self.isShoot = []
		self.laser = []
		self.enemy = []
		self.gameLevel = 10
		self.score = 0
		for i in range(10):
			self.enemy.append(Enemy(posX=random.randint(50, 750), posY=0))
			self.laser.append(Laser(posX=800, posY=600))
			self.isShoot.append(False)

	def init(self):
		super(DotShooter, self).init()
		self.render_score()

	def update(self):
		print "HP : %d ; Level : %d ; Score : %d" % (self.player.HP , self.gameLevel, self.score)

		for i in range(self.gameLevel):
			self.enemy[i].y += 3
			if self.isShoot[i]:
				self.laser[i].y -= 10
				self.checkCollision()
				if(self.laser[i].y < 0):
					self.isShoot[i] = False
			if(self.enemy[i].y >= 600):
				self.enemy[i].x = random.randint(50, 750)
				self.enemy[i].y = 0
				self.player.HP -= 1
				if(self.player.HP == 0):
					pass

		if self.is_key_pressed(K_SPACE):
			for i in range(self.gameLevel):
				if(self.isShoot[i] == False):
					if((i == 0) or (i > 0 and self.laser[i-1].y+200 < self.player.y)):
						self.isShoot[i] = True
						self.laser[i] = Laser(self.player.x, self.player.y)
						break
		elif self.is_key_pressed(K_LEFT):
			if(self.player.x > 20):
				self.player.move_left()
		elif self.is_key_pressed(K_RIGHT):
			if(self.player.x < 780):
				self.player.move_right()

	def render(self, surface):
		self.player.render(surface)

		for i in range(self.gameLevel):
			self.enemy[i].render(surface)
			if self.isShoot[i]:
				self.laser[i].render(surface)

	def render_score(self):
		self.score_image = self.font.render("Score = %d" % self.score, 20, DotShooter.WHITE)

	def checkCollision(self):
		for i in range(self.gameLevel):
			# print "Enemy %d : (%d, %d)" % (i, self.enemy[i].x, self.enemy[i].y)
			for j in range(self.gameLevel):
				# print "Laser %d : (%d, %d)" % (j, self.laser[j].x, self.laser[j].y)
				if(self.laser[j].y <= self.enemy[i].y and self.laser[j].y+20 >= self.enemy[i].y):
					# print "Check Y : Passed"
					if(self.laser[j].x-15 <= self.enemy[i].x and self.laser[j].x+15 >= self.enemy[i].x):
						# print "Check X : Passed"
						self.enemy[i].x = random.randint(50, 750)
						self.enemy[i].y = 0
						self.laser[j].x = 0
						self.laser[j].y = 0
						self.isShoot[j] = False
						self.score += 1

def main():
	game = DotShooter()
	game.run()

if __name__ == '__main__':
	main()