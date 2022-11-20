import pygame
import sys
from ship import Ship
from island import Island

pygame.init()

clock = pygame.time.Clock()

water = pygame.image.load('images/water.png')
water_rect = water.get_rect()
tile_size = water_rect.width
screen = pygame.display.set_mode((10*tile_size, 10*tile_size))
pygame.display.set_caption('Aargh')
screen.fill((0, 0, 0))

#load my island images
#top_left = pygame.image.load('images/topleft.png')
#top_mid = pygame.image.load('images/topmid.png')
#top_right = pygame.image.load('images/topright.png')
#bottom_left = pygame.image.load('images/bottomleft.png')
#bottom_mid = pygame.image.load('images/bottommid.png')
#bottom_right = pygame.image.load('images/bottomright.png')

island = Island()
island.move((320,320))

#load da ship
ship = Ship()

#add an oof
oof = pygame.mixer.Sound('oof.mp3')

#get screen rect parameters
screen_rect = screen.get_rect()

rows = screen_rect.height/tile_size
cols = screen_rect.width/tile_size

ship_coord = (0,0)

def draw_background():
    #drawing an ocean on the screen
    for x in range(int(rows)):
        for y in range(int(cols)):
            screen.blit(water, (x*water_rect.height, y*water_rect.width))

    #draw an island in the ocean
    island.draw(screen)
    #screen.blit(top_left, (screen_rect.centerx - 2*tile_size, screen_rect.centery - tile_size))
    #screen.blit(top_mid, (screen_rect.centerx - tile_size, screen_rect.centery - tile_size))
    #screen.blit(top_right, (screen_rect.centerx, screen_rect.centery - tile_size))
    #screen.blit(bottom_left, (screen_rect.centerx - 2*tile_size, screen_rect.centery))
    #screen.blit(bottom_mid, (screen_rect.centerx - 1*tile_size, screen_rect.centery))
    #screen.blit(bottom_right, (screen_rect.centerx, screen_rect.centery))

#draw the ship
#screen.blit(ship.image, (200,400))

#screen.blit(water, (168,168)) #referring to the upper left corner
#screen.blit(water, (0,0))
#screen.blit(water, (0,64))
#screen.blit(water, (64,0))

pygame.mouse.set_visible(False)



while True:
    #print("-----------------check for new events-----------------------")
    recent_events = pygame.event.get()
    #print("-----------------done checking for events----------------------")
    for event in recent_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            #draw_background()
            #print(event) - shows you where your mouse is coordinate-wise
            ship_coord = pygame.mouse.get_pos()
            #screen.blit(ship, ship_coord)

    draw_background()
    ship.move(ship_coord)

    #check collisions
    collision = pygame.sprite.collide_rect(ship, island)

    if collision:
        print(f"Steer clear of the island! Health: {ship.health}")
        pygame.mixer.Sound.play(oof)
        ship.health -= 1


    ship_rect = ship.rect
    ship.draw(screen)
    #ship_rect.center = ship_coord
    screen.blit(ship.image, ship_rect)
    pygame.display.flip()
    clock.tick(60)
