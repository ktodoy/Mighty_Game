import pygame

class Island:
    #create island constructor
    def __init__(self):
        #self.image = top_left = pygame.image.load('images/topleft.png')
        #self.rect = self.image.get_rect()

        self.image = pygame.surface.Surface((192, 128)) #makes the island one group/image
        self.image.blit(pygame.image.load('images/water.png'), (0, 0))
        self.image.blit(pygame.image.load('images/topleft.png'), (0, 0))
        self.image.blit(pygame.image.load('images/water.png'), (64, 0))
        self.image.blit(pygame.image.load('images/topmid.png'), (64, 0))
        self.image.blit(pygame.image.load('images/water.png'), (128, 0))
        self.image.blit(pygame.image.load('images/topright.png'), (128, 0))
        self.image.blit(pygame.image.load('images/water.png'), (0, 64))
        self.image.blit(pygame.image.load('images/bottomleft.png'), (0, 64))
        self.image.blit(pygame.image.load('images/water.png'), (64, 64))
        self.image.blit(pygame.image.load('images/bottommid.png'), (64, 64))
        self.image.blit(pygame.image.load('images/water.png'), (128, 64))
        self.image.blit(pygame.image.load('images/bottomright.png'), (128, 64))
        self.rect = self.image.get_rect()

    def move(self, coordinate):
        self.rect.center = coordinate

    def draw(self, surface):
        surface.blit(self.image, self.rect)
