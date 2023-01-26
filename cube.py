import pygame
import random

class Cube(pygame.sprite.Sprite):
    explosion = False
    def __init__(self):
        super().__init__()
    def draw(self, screen,x,y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x,self.y,16,16)
        pygame.draw.rect(screen, (255,255,255), self.rect)
        if self.explosion:
            pygame.draw.circle(screen, (255, 0, 0), [int(particle[0][0]), int(particle[1][1])], int(particle[2]))
    def explode(self, screen):
        particles = []
        particles.append([[250,250], [random.randint(0,20) / 10 - 1, -2], random.randint(4,6)])
        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            if particle[2] <= 0:
                particles.remove(particle)
            self.explosion = True



