import UDP_pc
import controller

while True:
    trig_left, trig_right, x_axis_left, \
        button_x, button_y, button_b, \
        button_a, button_select, button_start \
        = controller.get_controller_input()

    message = str(trig_left) + ":" + \
              str(trig_right) + ":" + \
              str(x_axis_left) + ":" + \
              str(button_x) + ":" + \
              str(button_y) + ":" + \
              str(button_b) + ":" + \
              str(button_a) + ":" + \
              str(button_select) + ":" + \
              str(button_start)


    UDP_pc.msg_send(message, "10.120.0.83", 5005)