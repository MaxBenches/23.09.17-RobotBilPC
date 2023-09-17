import pygame

# Allow controller input using pygame
pygame.joystick.init()

# Assign controller
controller = pygame.joystick.Joystick(0)
# Test - Print the assigned controller
#print(controller)

# Initialise pygame
pygame.init()

def controller_get_axes():
    while True:
        # Controller button input handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.JOYAXISMOTION:
                # Controller Analog Stick Input Handling
                x_axis = round(pygame.joystick.Joystick(0).get_axis(0), 2)
                y_axis = round(pygame.joystick.Joystick(0).get_axis(1), 2) * -1
                return x_axis, y_axis