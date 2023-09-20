import pygame

# Allow controller input using pygame
pygame.joystick.init()

# Assign controller
controller = pygame.joystick.Joystick(0)
# Test - Print the assigned controller
#print(controller)

# Initialise pygame
pygame.init()


def get_axis():
    while True:
        # Controller button input handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYBUTTONDOWN:
                # Controller Analog Stick Input Handling
                x_axis_left = controller.get_axis(0)
                left_trig = controller.get_axis(4) + 1  #Plus 1 to avoid negative values
                right_trig = controller.get_axis(5) + 1 #Plus 1 to avoid negative values
                button_x = controller.get_button(2)
                button_y = controller.get_button(3)
                return left_trig, right_trig, x_axis_left, button_x, button_y