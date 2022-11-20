import pygame

class Ship:
    #create ship constructor
    def __init__(self):
        self.healthy_image = pygame.image.load('images/ship.png')
        self.light_image = pygame.image.load('images/dship1.png')
        self.heavy_image  = pygame.image.load('images/dship2.png')
        self.destroy_image = pygame.image.load('images/dship3.png')
        self.image = self.healthy_image
        self.rect = self.image.get_rect()
        self.health = 200

    def move(self, coordinate):
        self.rect.center = coordinate

    def draw(self, surface):
        if self.health <= -400:
            self.image = self.destroy_image
            surface.blit(self.image, self.rect)
        elif self.health <= -200:
            self.image = self.heavy_image
            surface.blit(self.image, self.rect)
        elif self.health <= -0:
            self.image = self.light_image
            surface.blit(self.image, self.rect)