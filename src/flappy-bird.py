import pygame
import time
import os
import random
from Bird import Bird
from Pipe import Pipe
from Base import Base 

BGROUND_IMG = pygame.transform.scale(pygame.image.load(os.path.join("image","bg.png")).convert_alpha(), (600, 900))
WIN_WIDTH = 600
WIN_HEIGHT = 800
STAT_FONT = pygame.font.SysFont("comicsans", 50)

def draw_window(window, bird, pipes, base, score):
    window.blit(BGROUND_IMG, (0,0))

    for pipe in pipes:
        pipe.draw(window)
    base.draw(window)
    bird.draw(window)

    score_label = STAT_FONT.render("Score: " + str(score),1,(255,255,255))
    window.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15, 10))
    pygame.display.update()
def draw_gameover(window, label, score):

    score_label = STAT_FONT.render("Score: " + str(score),1,(255,255,255))
    window.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15, 10))
    pygame.display.update()
if __name__ == '__main__':
    bird = Bird(200, 200)
    base = Base(730)
    pipes = [Pipe(700)]
    window = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT)) 
    clock = pygame.time.Clock()
    score = 0
    run = True
    while run:
        clock.tick(30)
        keys=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                print("A key has been pressed")
                bird.jump()
        add_pipe = False
        rem = []
        for pipe in pipes:
            if pipe.collide(bird, window):
                run = False
                pass
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True
            pipe.move()
        if add_pipe:
            score +=1
            pipes.append(Pipe(700))
        for r in rem:
            pipes.remove(r)
        draw_window(window, bird, pipes, base, score)
        bird.move()
    pygame.quit()    
    quit()