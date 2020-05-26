import pygame

pygame.init() 

screen_info=pygame.display.Info()

screen_size=(width,height)=(screen_info.current_w, screen_info.current_h) 

fish_image=pygame.image.load("fish.png")
fish_image=pygame.transform.smoothscale(fish_image,(100,100))
fish_rect=fish_image.get_rect()
fish_rect.center=(width//2,height//2)

speed=pygame.math.Vector2(0,10)
roation=random.randint(0,360)

def move_fish():
  global fish_image 
  screen_info=pygame.display.Info() 
  fish_rect.move_ip(speed) 
  if fish_rect.left <= 0 or fish_rect.right > screen_info.current_w:

screen=pygame.display.set_mode(screen_size)
color=(153,204,7) 

def main():
  while True:
    screen.fill(color)
    screen.blit(fish_image,fish_rect)
    pygame.display.flip()


if __name__ == '__main__':
  main()

#print(screen_info.current_w)
#print(screen_info.current_h)