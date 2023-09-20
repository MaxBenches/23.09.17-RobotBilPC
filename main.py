import UDP_pc
import controller

while True:
    left_trig, right_trig, x_axis_left, button_x, button_y = controller.get_axis()
    message = str(left_trig) + ":" + str(right_trig) + ":" + \
              str(x_axis_left) + ":" + str(button_x) + ":" + str(button_y)

    print(message)
    UDP_pc.msg_send(message, "192.168.0.166", 5005)