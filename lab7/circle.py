import pygame
pygame.init()



WIDTH,HEIGHT = 1048,1048
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
BLACK = (0,0,0)


def draw_circle(x,y):
        WIN.fill((WHITE))
        pygame.draw.circle(WIN,(0,0,0),(x,y), 25, 5)
        pygame.display.update()



def main():
    run = True
    x = 50
    y = 50
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        draw_circle(x,y)

        if keys[pygame.K_UP] and y > 50:
             y-=20
        if keys[pygame.K_LEFT] and x > 50:
             x-=20
        if keys[pygame.K_DOWN] and y < 950:
             y+=20
        if keys[pygame.K_RIGHT] and x < 1000:
             x+=20


    pygame.quit()


if __name__ == "__main__":
    main()