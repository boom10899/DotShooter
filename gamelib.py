import pygame
from pygame.locals import *

class SimpleGame(object):

	def __init__(self, title, background_color, window_size=(800,600), fps=60):
		self.title = title
		self.window_size = window_size
		self.fps = fps

		self.is_terminated = False
		self.background_color = background_color

	def __game_init(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.surface = pygame.display.set_mode(self.window_size)
		pygame.display.set_caption(self.title)
		self.font = pygame.font.SysFont("monospace", 20)

	def init(self):
		self.__game_init()

	def run(self):
		self.init()
		while not self.is_terminated:
			self.__handle_events()
			self.update()
			self.surface.fill(self.background_color)
			self.render(self.surface)
			pygame.display.update()
			self.clock.tick(self.fps)

	def update(self):
		pass

	def render(self, surface):
		pass

	def is_key_pressed(self, key):
		keys_pressed = pygame.key.get_pressed()
		if key < 0 or key >= len(keys_pressed):
			return False
		return (keys_pressed[key])

	def __handle_events(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.terminate()

	def terminate(self):
		self.is_terminated = True