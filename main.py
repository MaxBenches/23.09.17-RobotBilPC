import UDP_pc
import controller

while True:
    x_axis, y_axis = controller.controller_get_input()
    message = str(x_axis) + ":" + str(y_axis)
    print(message)
    UDP_pc.msg_send(message, "10.120.0.18", 5005)