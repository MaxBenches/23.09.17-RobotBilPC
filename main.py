import UDP_pc
import controller

while True:
    trig_left, trig_right, x_axis_left, button_x, button_y, button_b = controller.get_controller_input()
    message = str(trig_left) + ":" + \
              str(trig_right) + ":" + \
              str(x_axis_left) + ":" + \
              str(button_x) + ":" + \
              str(button_y) + ":" + \
              str(button_b)

    print(trig_left, trig_right)
    UDP_pc.msg_send(message, "192.168.0.166", 5005)