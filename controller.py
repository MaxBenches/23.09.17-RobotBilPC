import pygame

# Allow controller input using pygame
pygame.joystick.init()

# Assign controller
controller = pygame.joystick.Joystick(0)
# Test - Print the assigned controller
#print(controller)

# Initialise pygame
pygame.init()


def get_controller_input():
    while True:
        # Controller button input handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYBUTTONDOWN:
                # Controller Analog Stick Input Handling
                x_axis_left = controller.get_axis(0)
                trig_left = controller.get_axis(4)
                trig_right = controller.get_axis(5)
                button_x = controller.get_button(2)
                button_y = controller.get_button(3)
                button_b = controller.get_button(1)
                button_a = controller.get_button(0)
                button_select = controller.get_button(6)
                button_start = controller.get_button(7)
                return trig_left, trig_right, x_axis_left, \
                    button_x, button_y, button_b, \
                    button_a, button_select, button_start
