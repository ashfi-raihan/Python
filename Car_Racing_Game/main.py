import pygame
import time
import math
from util import scale_image, blit_rotate_center

# CAPITAL means the variables are cons
# set the images in the variables
GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.75)

TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.75)
TRACK_BORDER_MASK= pygame.mask.from_surface(TRACK_BORDER) # learn mask from 2nd video
FINISH = pygame.image.load("imgs/finish.png")
FINISH_MASK = pygame.mask.from_surface(FINISH)
FINISH_POSITON = (100, 250)

RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.45)
GREEN_CAR = scale_image(pygame.image.load("imgs/green-car.png"), 0.45)

# setup the display with the size of the display

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")

# display imgs
FPS = 30 #  frame per sec

# function for the common functionality of the both cars 
class AbstractCar():
    
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x , self.y = self.START_POS
        self.acceleration = 0.1 

    def rotate(self, left = False, right = False):
        if left: 
            self.angle += self.rotation_vel
        elif right: 
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel) # this will stop the valocity from increasing when it is maximum
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2) 
        self.move()
          
    # description in video-1 41:00 min
    def move(self):
        radians = math.radians(self.angle)
        verticle = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= verticle
        self.x -= horizontal
    
    def reduced_speed(self):
        self.vel = max (self.vel - self.acceleration/2 , 0)
        self.move()

    # from second video
    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y-y))
        poi = mask.overlap(car_mask, offset)
        return poi 
    
    def reset(self):
        self.x , self.y = self.START_POS
        self.angle = 0
        self.vel = 0



class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (140, 200)

    def bounce(self):
        self.vel = -self.vel
        self.move()

# to draw the images in the window
def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)
    
    player_car.draw(win)
    pygame.display.update()

def move_player(player_car):
    # key Event
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_LEFT]: # when you press 'left'
        player_car.rotate(left=True)
    if keys[pygame.K_RIGHT]: # when you press 'right'  
        player_car.rotate(right=True)
    if keys[pygame.K_UP]: # when you press 'up'  
        moved = True
        player_car.move_forward()
    if keys[pygame.K_DOWN]: # when you press 'down'  
        moved = True
        player_car.move_backward()

    if not moved: 
        player_car.reduced_speed()


#images = [(GRASS,(0,0)), (TRACK, (0,0)), (RED_CAR,(0,0)), (GREEN_CAR, (10,0))]
images = [(GRASS,(0,0)), (TRACK, (0,0)), (FINISH, FINISH_POSITON), (TRACK_BORDER, (0,0))]

run = True # to stop the programe in future
clock = pygame.time.Clock() # to fix the velocity with the time or ek ek device e ek ek velocity ashbe

player_car = PlayerCar(4,4)

while run: 
    clock.tick(FPS) # the car cannot run faster then 60 fps

    # shows the img in the screen
    draw(WIN, images, player_car)  


    for event in pygame.event.get():  # get all the events in the pygame
        if event.type == pygame.QUIT:
            run = False
            break
    
    move_player(player_car)
    if player_car.collide(TRACK_BORDER_MASK) != None: 
        player_car.bounce()
    
    finish_poi_collide = player_car.collide(FINISH_MASK, *FINISH_POSITON)
    if finish_poi_collide != None:
        if finish_poi_collide[1] == 0:
            player_car.bounce()
        else: 
            player_car.reset()


pygame.quit()
