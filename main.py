import UDP_pc
import controller

while True:
    x, y = controller.controller_get_axes()
    message = x, y
    print(message)
    UDP_pc.msg_send(message, "192.168.0.226", 5005)