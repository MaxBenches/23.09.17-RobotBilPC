import pygame

# Allow controller input using pygame
pygame.joystick.init()

# Assign controller
controller = pygame.joystick.Joystick(0)
# Test - Print the assigned controller
#print(controller)

# Initialise pygame
pygame.init()


def controller_get_input():
    while True:
        # Controller button input handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.JOYAXISMOTION:
                # Controller Analog Stick Input Handling
                x_axis = pygame.joystick.Joystick(0).get_axis(0)
                #y_axis = round(pygame.joystick.Joystick(0).get_axis(1) * -1)
                left_trig = pygame.joystick.Joystick(0).get_axis(4) + 1
                right_trig = pygame.joystick.Joystick(0).get_axis(5) + 1
                return left_trig, right_trig, x_axis
            """
            if event.type == pygame.JOYBUTTONDOWN:
                button_y = pygame.joystick.Joystick(0).get_button(3)
                return button_y
            """