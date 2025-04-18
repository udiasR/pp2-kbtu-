import pygame
import datetime
pygame.init()


WIDTH,HEIGHT = 800,800
WHITE = (255,255,255)
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60

y = 0

CLOCK_IMAGE = pygame.transform.scale(pygame.image.load("./images/clock.png"),(WIDTH,HEIGHT))
LEFT_IMAGE = pygame.transform.scale(pygame.image.load("./images/leftarm.png"),(WIDTH//15,HEIGHT//2))
RIGHT_IMAGE = pygame.transform.scale(pygame.image.load("./images/rightarm.png"),(WIDTH,HEIGHT))


text1 = 16
text2 = 00


def draw_window(text1, text2):
    font = pygame.font.SysFont(None, 100)  
    # WIN.blit(CLOCK_IMAGE,(0,0))
    
    
    now = datetime.datetime.now()
    dateoftime = (now.strftime("%d-%m-%Y"))
    date = pygame.draw.rect("f{dateoftime}", (255,255,255))
 
        
    left_rotated = pygame.transform.rotate(LEFT_IMAGE, left_angle)
    right_rotated = pygame.transform.rotate(RIGHT_IMAGE, right_angle)

    
    left_x = WIDTH // 2 - left_rotated.get_width() // 2
    left_y = HEIGHT // 2 - left_rotated.get_height() // 2

    right_x = WIDTH // 2 - right_rotated.get_width() // 2
    right_y = HEIGHT // 2 - right_rotated.get_height() // 2

    WIN.blit(left_rotated, (left_x, left_y))
    WIN.blit(right_rotated, (right_x, right_y))

    pygame.display.update()


def main():
    run  = True
    left_angle =0
    right_angle =320
    clock= pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run  = False
        clock.tick(FPS)
        now = datetime.datetime.now()
        dateoftime = (now.strftime("%d-%m-%Y"))
        print(now)
        
        WIN.blit(date, (50,50))
        pygame.display.update()
        left_angle -= 1/6 
        right_angle -= 1/36
        draw_window(left_angle, right_angle)
    
    pygame.quit()

if __name__ == "__main__":
    main()