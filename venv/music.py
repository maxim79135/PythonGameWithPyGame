import pygame

soundObj = pygame.mixer.Sound('venv/Beep.mp3')
soundObj.play()
import time
time.sleep(1)
soundObj.stop()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()