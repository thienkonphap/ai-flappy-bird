import pygame
import os


BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("image","base.png")).convert_alpha())

class Base: 
    
    VEL = 5
    WIDTH  = BASE_IMG.get_width()
    IMP = BASE_IMG
    def __init__(self,y):
        self.WIDTH  = BASE_IMG.get_width()
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH
    def move(self):
        self.x1 -= 5
        self.x2 -= 5
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH
    def draw(self, window):
        window.blit(BASE_IMG, (self.x1, self.y))
        window.blit(BASE_IMG, (self.x2, self.y))
