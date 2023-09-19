import UDP_pc
import controller

while True:
    left_trig, right_trig, x_axis = controller.controller_get_input()
    message = str(left_trig) + ":" + str(right_trig) + ":" + str(x_axis)
    print(message)
    UDP_pc.msg_send(message, "10.120.0.83", 5005)