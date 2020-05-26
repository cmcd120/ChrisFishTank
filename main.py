import pygame

pygame.init() 

screen_info=pygame.display.Info()

screen_size=(width,height)=(screen_info.current_w, screen_info.current_h) 

screen=pygame.display.set_mode(screen_size)
color=(153,204,7) 

def main():
  while True:
    screen.fill(color)
    pygame.display.filp()


if_name_=='_main_':
  main()

#print(screen_info.current_w)
#print(screen_info.current_h)