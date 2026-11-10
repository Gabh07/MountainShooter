import pygame

print('Setup Start')
pygame.init()

# Criate window
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop Start')

# For window to stay open
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitting...')
            pygame.quit() # Close Window
            quit() # End pygame
