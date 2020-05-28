import sys, pygame
from pygame.locals import *
from fish import *
from pacman import *

pygame.init()

screen_info = pygame.display.Info()
screen_size = (screen_info.current_w, screen_info.current_h)

size = (width, height) = (850, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

color = (0, 127, 255)
textColor=(50,254,30)
txtBackgroundColor=(94,0,4)
fishes = pygame.sprite.Group()

Player=Pacman((150,150))

font=pygame.font.Font('freesansbold.ttf',32)
text=font.render("Hello",True,textColor,txtBackgroundColor)
textRect = text.get_rect()
textRect.center = (width // 2, height // 2)  


def main():
    for i in range(10):
        fishes.add(Fish((width / 2, height / 2)))
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                fishes.add(Fish(event.pos))
            if event.type == KEYUP:
                if event.key == K_UP:
                  Player.speed[1]=0 
                if event.key == K_DOWN:
                  Player.speed[1]=0  
                if event.key==K_LEFT:
                  Player.speed[0]=0
                if event.key==K_RIGHT:
                  Player.speed[0]=0
            if event.type == KEYDOWN:
                if event.key == K_UP:
                  Player.speed[1]=-10 
                if event.key == K_DOWN:
                  Player.speed[1]=10  
                if event.key==K_LEFT:
                  Player.speed[0]=-10
                if event.key==K_RIGHT:
                  Player.speed[0]=10
                
                
                if event.key == K_d:
                    for i in range(len(fishes) // 2):
                        fishes.pop(0)
                if event.key == K_f:
                    pygame.display.set_mode(screen_size, FULLSCREEN)
                if event.key == K_ESCAPE:
                    pygame.display.set_mode(size)
        screen.fill(color)
        for fish in fishes:
            fish.update()
        for fish in fishes:
            fish.draw(screen)
        Player.update()
        get_hit=pygame.sprite.spritecollide(Player,fishes, False) 
        screen.blit(Player.image,Player.rect)
        if get_hit:
          screen.blit(text,textRect)
        pygame.display.flip()


if __name__ == '__main__':
    main()