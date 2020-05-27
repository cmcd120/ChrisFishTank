import pygame, random, sys
from pygame.locals import *

pygame.init() 

screen_info=pygame.display.Info()

screen_size=(width,height)=(screen_info.current_w, screen_info.current_h) 

#Clock to set frame rate 
clock=pygame.time.Clock()

fish_image=pygame.image.load("fish.png")
fish_image=pygame.transform.smoothscale(fish_image,(100,100))
fish_rect=fish_image.get_rect()
fish_rect.center=(width//2,height//2)

#variables to move fish
speed=pygame.math.Vector2(30,5)
rotation=random.randint(0,360)
speed.rotate_ip(rotation)
color=(153,204,7) 
screen=pygame.display.set_mode(screen_size)

fish_image=pygame.transform.rotate(fish_image,180-rotation)

#define what happens when we move the fish
def move_fish():
  global fish_image 
  screen_info=pygame.display.Info() 
  fish_rect.move_ip(speed)  


  #if fish hits top or bottom
  if fish_rect.top < 0 or fish_rect.bottom > screen_info.current_h:
    speed[1] *= -1
    fish_rect.move_ip(0, speed[1])
    fish_image=pygame.transform.flip(fish_image, True, False)

 #if fish hits left or right
  if fish_rect.left < 0 or fish_rect.right > screen_info. current_w:
    speed[0] *= -1
    fish_rect.move_ip(speed[0], 0) 
    fish_image=pygame.transform.flip(fish_image, False, True)


  #if fish_rect.left <= 0 or fish_rect.right > screen_info.current_w:

#click
#button PRESS 
#hover 



#main game loop
def main():
  while True: 
    clock.tick(60)

    for event in pygame.event.get():
      if event.type==QUIT:
        sys.exit()
      #if event.type==MOUSEBUTTONDOWN:
        #speed[1]=0 
        #speed[0]=0
      if event.type==KEYDOWN: 
        if event.key==K_s: 
          speed[1]=0
          speed[0]=0
        if event.key==K_g: 
          speed[1]=15
          speed[0]=0



    move_fish()
    screen.fill(color)
    screen.blit(fish_image,fish_rect)
    pygame.display.flip()

#necessary code 
if __name__ == '__main__':
  main()

#print(screen_info.current_w)
#print(screen_info.current_h)