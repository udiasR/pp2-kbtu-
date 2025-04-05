# import pygame
# #music = background
# #sound effects = play when we call it

# pygame.init()

# WIDTH, HEIGHT = 800,800
# FPS = 60
# HITSOUND = pygame.mixer.Sound("Bylygyp.mp3")
# BYLYGYP = pygame.mixer.Sound("Bylygyp.mp3")
# EnSulu = pygame.mixer.Sound("En-sulu.mp3")

# music = pygame.mixer.music.load("En-sulu.mp3")

# #HITSOUND.play()
# pygame.mixer.music.play(-1)      #infinite







# WIN = pygame.display.set_mode((WIDTH,HEIGHT))
# BACK = pygame.image.load("back.png")
# NEXT = pygame.image.load("next.png")
# PAUSE = pygame.image.load("pause.png")
# PLAY = pygame.image.load("play.png")

# playlist=  ["Bylygyp.mp3","En-sulu.mp3"]
# current_track = 0
# pygame.mixer.music.load(playlist[current_track])
# pygame.mixer.music.play(-1)

# # playlist.append(EnSulu)
# # playlist.append(BYLYGYP)




# def draw_window():
#     WIN.fill((255,255,255))
#     pygame.display.update()




# def main():
#     run  = True
#     clock = pygame.time.Clock()
#     while run:
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
    
#         clock.tick(FPS)
#         draw_window()
#         keys = pygame.key.get_pressed()
#         # if keys[pygame.K_SPACE]:
#         #     for x in playlist:
#         #         playlist[x].play()
#         # if keys[pygame.K_LEFT]:
#         #     for x in playlist:
#         #         playlist[x+1].play()

#         #         if keys[pygame.K_SPACE]:
#         #     HITSOUND.play()

#         # Go to next track
#         if keys[pygame.K_RIGHT]:
#             current_track = (current_track + 1) % len(playlist)
#             pygame.mixer.music.load(playlist[current_track])
#             pygame.mixer.music.play(-1)
#             pygame.time.wait(200)  # avoid multiple quick switches

#         # Go to previous track
#         if keys[pygame.K_LEFT]:
#             current_track = (current_track - 1) % len(playlist)
#             pygame.mixer.music.load(playlist[current_track])
#             pygame.mixer.music.play(-1)
#             pygame.time.wait(200)

#         # Pause/play toggle
#         if keys[pygame.K_p]:
#             if not paused:
#                 pygame.mixer.music.pause()
#                 paused = True
#             else:
#                 pygame.mixer.music.unpause()
#                 paused = False
#             pygame.time.wait(200)

#     pygame.quit()

# if __name__ == "__main__":
#     main()



import pygame
import os

# Initialize Pygame and Mixer
pygame.init()
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Keyboard-Controlled Music Player")

# Music Playlist (put your MP3 files in the same directory)
playlist = ["En-sulu.mp3", "Bylygyp.mp3"]
current_track = 0
is_paused = False

# Load the first track
pygame.mixer.music.load(playlist[current_track])

# Helper: Display track name
font = pygame.font.SysFont("Arial", 30)

def draw_window(track_name):
    WIN.fill((30, 30, 30))
    text = font.render(f"Now Playing: {track_name}", True, (255, 255, 255))
    WIN.blit(text, (50, HEIGHT // 2))
    pygame.display.update()

def main():
    global current_track, is_paused

    clock = pygame.time.Clock()
    run = True

    draw_window(os.path.basename(playlist[current_track]))

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        # Play/Pause toggle
        if keys[pygame.K_p]:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
                is_paused = True
            elif is_paused:
                pygame.mixer.music.unpause()
                is_paused = False
            else:
                pygame.mixer.music.play()
            pygame.time.wait(200)

        # Stop music
        if keys[pygame.K_s]:
            pygame.mixer.music.stop()
            is_paused = False
            pygame.time.wait(200)

        # Next track
        if keys[pygame.K_RIGHT]:
            current_track = (current_track + 1) % len(playlist)
            pygame.mixer.music.load(playlist[current_track])
            pygame.mixer.music.play()
            is_paused = False
            draw_window(os.path.basename(playlist[current_track]))
            pygame.time.wait(200)

        # Previous track
        if keys[pygame.K_LEFT]:
            current_track = (current_track - 1) % len(playlist)
            pygame.mixer.music.load(playlist[current_track])
            pygame.mixer.music.play()
            is_paused = False
            draw_window(os.path.basename(playlist[current_track]))
            pygame.time.wait(200)

    pygame.quit()

if __name__ == "__main__":
    main()
