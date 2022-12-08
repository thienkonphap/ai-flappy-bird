import pygame
import os

pygame.init()
WIN_WIDTH = 600
WIN_HEIGHT = 800

MAX_ROTATION = 25
ROT_VEL = 20
ANIMATION_TIME = 5
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("image","pipe.png")).convert_alpha())
BGROUND_IMG = pygame.transform.scale(pygame.image.load(os.path.join("image","bg.png")).convert_alpha(), (600, 900))
BIRD_IMG = [pygame.transform.scale2x(pygame.image.load(os.path.join("image","bird" + str(x) + ".png"))) for x in range(1,4)]
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("image","base.png")).convert_alpha())
class Bird:
    IMG = BIRD_IMG
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = y 
        self.img_count  = 0
        self.img = BIRD_IMG[0]
    def jupmp(self):
        self.vel = -12.5 # (0.0) is top left of the screen 
        self.tick_count = 0
        self.height = y
    
    def move(self):
        self.tick_count += 1

        # for downward acceleration
        displacement = self.vel*(self.tick_count) + 0.5*(3)*(self.tick_count)**2  # calculate displacement

        # terminal velocity
        if displacement >= 16:
            displacement = (displacement/abs(displacement)) * 16

        if displacement < 0:
            displacement -= 2

        self.y = self.y + displacement

        if displacement < 0 or self.y < self.height + 50:  # tilt up
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:  # tilt down
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL
    def draw(self, win):
        self.img_count += 1
        # For animation of bird, loop through three images
        if self.img_count <= self.ANIMATION_TIME:
            self.img = BIRD_IMG[0]
        elif self.img_count <= self.ANIMATION_TIME*2:
            self.img = BIRD_IMG[1]
        elif self.img_count <= self.ANIMATION_TIME*3:
            self.img = BIRD_IMG[2]
        elif self.img_count <= self.ANIMATION_TIME*4:
            self.img = BIRD_IMG[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = BIRD_IMG[0]
            self.img_count = 0
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft) # rotate image
    def get_mask(self):
        return pygame.mask.from_surface(self.img)
    def jump(self):
        """
        make the bird jump
        :return: None
        """
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y